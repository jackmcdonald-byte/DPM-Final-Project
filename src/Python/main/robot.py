from chassis import Chassis
from navigation import Navigation
from sensors import SensorController
from siren import Siren

import colour_processing


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
        self.chassis = Chassis()
        self.navigation = Navigation()
        self.sensors = SensorController()
        self.siren = Siren()
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
            # TODO Stop all robot functions here
            pass

    def __create_threads(self):
        pass

    def __enter_navigation_a(self):
        pass

    def __enter_search(self):
        pass

    def __enter_navigation_b(self):
        pass
