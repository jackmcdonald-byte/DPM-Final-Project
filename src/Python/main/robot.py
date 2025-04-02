import sys
from threading import *
from chassis import Chassis
from navigation import Navigation
from sensors import SensorController
from siren import Siren


class Robot:
    """
    Controls the operation of a robotic system, managing its state transitions,
    subsystems, and behaviors. It includes methods to initialize, start,
    stop, and manage the robot's internal states and interactions between
    its various subsystems such as chassis, navigation, sensors, and siren.

    :ivar state: Current operational state of the robot.
    :type state: str
    :ivar chassis: Handles the physical movement and drive mechanisms.
    :type chassis: Chassis
    :ivar navigation: Manages navigation and pathfinding routines.
    :type navigation: Navigation
    :ivar sensors: Controls and processes data from sensing hardware.
    :type sensors: SensorController
    :ivar siren: Controls the siren functionality for signaling or warnings.
    :type siren: Siren
    Author: Jack McDonald
    """

    def __init__(self):
        """
        Represents the main controller for a robotic system, initializing key components
        and managing the overall state. This class is responsible for orchestrating
        different subsystems such as chassis, navigation, sensors, and the siren, while
        maintaining an internal state to track system activity.

        Attributes
        ----------
        state : str
            The current state of the robotic system, initially set to "idle".
        chassis : Chassis
            The subsystem responsible for managing the robot's movement and driving.
        navigation : Navigation
            The subsystem responsible for navigational tasks, pathfinding, and
            orientation.
        sensors : SensorController
            Manages the robot's sensor modules for detecting environmental data and
            obstacles.
        siren : Siren
            Controls the siren mechanism of the robot.
        """
        self.state = "idle"
        self.chassis = Chassis(self)
        self.navigation = Navigation()
        self.sensors = SensorController()
        self.siren = Siren()

        self.sensor_thread = None
        self.emergency_stop_thread = None

        self.colour_reading = ""
        self.distance_reading = -1
        self.touch_reading = False

        self.__create_threads()

    def run(self):
        """
        Transitions through a sequence of states and invokes corresponding entry methods.

        The `run` function interacts with the user via an `input` prompt to signal the
        beginning of the operation and manages transitions between states within the system.
        It sequentially enters the `NavigationA`, `Search`, and `NavigationB` phases,
        invoking private methods associated with each state transition for handling specific
        behaviors in those states. Errors related to input/output operations are caught
        and displayed to the user.

        Author: Jack McDonald
        """
        input("Press Enter to begin...")
        try:
            self.__transition_to("initializing")
            self.sensor_thread.start()
            self.emergency_stop_thread.start()

            self.__transition_to("NavigationA")
            self.__enter_navigation_a()

            self.__transition_to("Search")
            self.__enter_search()

            self.__transition_to("NavigationB")
            self.__enter_navigation_b()
        except IOError as error:
            print(error)


    def stop(self):
        """
        Stops the current process or operation and transitions the state of the object
        to "idle". This method attempts to change the state regardless of the current
        state, handling potential input/output errors during the process.

        Author: Jack McDonald
        """
        try:
            self.__transition_to("idle")

            # Wait for threads to terminate
            if self.sensor_thread and self.sensor_thread.is_alive():
                self.sensor_thread.join()
            if self.emergency_stop_thread and self.emergency_stop_thread.is_alive():
                self.emergency_stop_thread.join()

            print("Robot stopped, threads terminated")
        except IOError as error:
            print(error)


    def __transition_to(self, new_state: str) -> None:
        self.__exit_state()
        self.state = new_state
        self.__enter_state()

    def __exit_state(self) -> None:
        if self.state == "NavigationA":
            self.siren.stop_siren()

    def __enter_state(self) -> None:
        if self.state == "NavigationA":
            self.siren.play_siren()
        if self.state == "idle":
            sys.exit() # TODO find better solution
            pass

    def __create_threads(self):
        self.sensor_thread = Thread(target=self.__update_sensor_data, daemon=True, name="sensors")
        self.emergency_stop_thread = Thread(target=self.__emergency_stop_check, daemon=True, name="em._stop")

    def __enter_navigation_a(self):
        self.chassis.move_until_colour("yellow")
        self.chassis.turn_right()
        self.chassis.move_until_distance(25)
        self.chassis.turn_left()

    def __enter_search(self):
        # TODO temp code
        while self.navigation.found < 2:
            if self.colour_reading == "red":
                self.chassis.extinguish_fire()
                self.chassis.MotorController.move_distance_forward(20, 100)
                self.navigation.found += 1

    def __enter_navigation_b(self):
        self.chassis.move_until_colour("yellow")
        self.chassis.turn_right()
        self.chassis.move_until_distance(3)
        self.chassis.turn_left()
        self.chassis.move_until_distance(3)

    def __update_sensor_data(self):
        while self.state != "idle":
            self.colour_reading = self.sensors.get_colour_name()
            self.distance_reading = self.sensors.get_us_sensor_distance()
            self.touch_reading = self.sensors.get_touch_sensor_state()

    def __emergency_stop_check(self):
        while self.state != "idle":
            if self.touch_reading:
                self.stop()

    def get_distance(self):
        return self.distance_reading