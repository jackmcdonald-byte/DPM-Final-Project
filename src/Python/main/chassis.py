from motor import MotorController
import time

# define constants pertaining to robot turning (in the functions turn_right(), turn_left(), and turn_around())
LEFT = -90  # positive constant for left turn
RIGHT = 90  # negative constant for right turn
AROUND = 180

# Constants for movement tuning
OVERRUN_DISTANCE = 15  # meters to move past the line (adjust based on robot size)
ROLLBACK_DISTANCE = 0.12
EXTINGUISH_DISTANCE = 0.04
TIMEOUT = 5  # timeout constant for one tile forward move


class Chassis:
    """
    Manages the movement and control of a robotic chassis.

    This class provides functionality to move the robot in various
    ways, such as moving until a specific condition is met (e.g. a
    particular color or distance), turning in different directions,
    moving a set distance (one tile), and performing specialized
    actions like fire extinguishment. It interfaces with the
    MotorController for managing motor operations.

    :ivar MotorController: Handles the motor operations for the chassis.
    :type MotorController: MotorController
    Authors: Jack McDonald, Ralph Calabrese
    """

    def __init__(self, robot):
        """
        Initializes the Chassis class and its dependencies.
        
        This constructor links the chassis with its motor control
        system and validates the provided robot instance.
        
        :param robot: The robot instance to associate with the chassis.
        :type robot: Robot
        :raises TypeError: If the provided `robot` is not an instance of the Robot class.
        """
        from robot import Robot
        if not isinstance(robot, Robot):
            raise TypeError("Expected an instance of Robot.")

        self.MotorController = MotorController()
        self.robot = robot

    def move_until_colour(self, colour: str):
        """
        Moves the robot forward until the specified colour is detected.
        
        The robot continuously moves forward while checking its colour sensor.
        Once the target colour is detected, the robot halts, rolls back slightly,
        and stops.
        
        :param colour: The target colour to detect.
        :type colour: str
        :return: None
        """
        self.MotorController.move_forward()
        while self.robot.get_colour() != colour:
            pass
        self.MotorController.stop()
        time.sleep(0.3)
        self.MotorController.move_distance_forward(distance=-ROLLBACK_DISTANCE,
                                                   speed=self.MotorController.FWD_SPEED / 1.4)
        time.sleep(0)
        self.MotorController.stop()

    def move_until_distance(self, distance: int):
        """
        Moves the robot forward until an object is within a specified distance.
        
        The robot continues moving forward until its sensors detect an object
        closer than or equal to the given distance in centimeters. If a red
        colour is detected in the "Search" state, it triggers fire extinguishment.
        
        :param distance: Maximum distance in centimeters to stop moving.
        :type distance: int
        :return: None
        """

        self.MotorController.move_forward()
        while self.robot.get_distance() > distance and self.robot.get_distance() != 0:
            if self.robot.get_colour() == "red" and self.robot.state == "Search":
                self.MotorController.stop()
                self.extinguish_fire()
                self.robot.navigation.found += 1
                self.MotorController.move_forward()
        self.MotorController.stop()

    def move_one_tile(self):
        """
        Moves the robot forward by one tile using the colour sensor.
        
        The robot first detects and crosses a black line, then travels a
        specified overrun distance before stopping.
        
        :return: None
        """
        # Move forward until black line is detected
        self.move_until_colour("black")

        # Move past the line by specified overrun distance
        self.move_until_distance(OVERRUN_DISTANCE)

    def turn_right(self):
        """
        Rotates the robot 90 degrees to the right.
        
        This method adjusts the motor system to turn the robot to the
        right by the specified angle.
        
        :return: None
        """
        self.MotorController.rotate(angle=RIGHT,
                                    speed=self.MotorController.TRN_SPEED)

    def turn_left(self):
        """
        Rotates the robot 90 degrees to the left.
        
        This method adjusts the motor system to turn the robot to the
        left by the specified angle.
        
        :return: None
        """
        self.MotorController.rotate(angle=LEFT,
                                    speed=self.MotorController.TRN_SPEED)

    def turn_around(self):
        """
        Rotates the robot 180 degrees to reverse its direction.
        
        This method performs a full rotation to allow the robot to
        face the opposite direction.
        
        :return: None
        """
        self.MotorController.rotate(angle=AROUND,
                                    speed=self.MotorController.TRN_SPEED)

    def extinguish_fire(self):
        """
        Activates the robot's fire-extinguishing mechanism.
        
        The robot reverses slightly, dispenses the fire suppressant,
        and returns to its original position.
        
        :return: None
        """
        # Activate dispenser
        self.MotorController.move_distance_forward(distance=-EXTINGUISH_DISTANCE,
                                                   speed=self.MotorController.FWD_SPEED / 2)
        self.MotorController.dispense()
        input("Press Enter to continue...")
        self.MotorController.move_distance_forward(distance=EXTINGUISH_DISTANCE,
                                                   speed=self.MotorController.FWD_SPEED / 2)

    def move_distance_forward(self, distance: int):
        """
        Moves the robot forward by a specific distance.
        
        The robot moves a fixed distance forward at the motor's configured speed.
        
        :param distance: The distance to move forward, in meters.
        :type distance: int
        :return: None
        """
        self.MotorController.move_distance_forward(distance=distance, speed=self.MotorController.FWD_SPEED)

    def turn_degrees(self, degrees: int):
        """
        Rotates the robot by a specified number of degrees.
        
        The robot rotates either clockwise or counterclockwise, depending 
        on the value of the degrees parameter.
        
        :param degrees: The angle to rotate in degrees (positive for clockwise, negative for counterclockwise).
        :type degrees: int
        :return: None
        """
        self.MotorController.rotate(angle=degrees, speed=self.MotorController.TRN_SPEED)

    def move_distance_forward_slow(self, param):
        """
        Moves the robot forward slowly by a specific distance.
        
        The robot advances forward at half its normal speed.
        
        :param param: The distance to move forward, in meters.
        :type param: int
        :return: None
        """
        self.MotorController.move_distance_forward(distance=param, speed=self.MotorController.FWD_SPEED / 2)

    def move_until_line(self):
        """
        Moves the robot forward slowly until it detects a black or grey line.
        
        This method polls the robot's colour sensor and halts when the
        specified line is detected.
        
        :return: None
        """
        self.MotorController.move_forward_slow()
        while self.robot.get_colour() != "black" or self.robot.get_colour() != "grey":
            pass
        self.MotorController.stop()
