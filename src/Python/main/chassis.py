from robot import Robot
from motor import MotorController
import time

# define constants pertaining to robot turning (in the functions turn_right(), turn_left(), and turn_around())
LEFT = 90  # positive constant for left turn
RIGHT = -90  # negative constant for right turn
AROUND = 180

# Constants for movement tuning
OVERRUN_DISTANCE = 15  # cms to move past the line (adjust based on robot size)
HALF_TILE_DISTANCE = 15 # cms to move backwards after stopping when purple is detected (adjust given tile size)
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
        Represents the main class responsible for initializing the 
        MotorController object. This class serves as the entry point 
        to create an instance of the MotorController and link it 
        to its functionalities.

        :Attributes:
            MotorController (MotorController): An instance of the 
            MotorController class, initialized when creating this class.
        Author: Jack McDonald
        """
        self.MotorController = MotorController()
        self.robot = robot

    def move_until_colour(self, colour: str):
        """
        Moves the robot until the specified colour is detected. The movement stops when the given
        colour is identified. This function assumes a mechanism to detect colours and halts operation
        when the desired condition is fulfilled.

        :param colour: The target colour to be detected during the movement.
        :type colour: str
        :return: None
        """
        self.MotorController.move_forward()
        while self.robot.get_colour() != colour:
            pass
        self.MotorController.stop()

    def move_until_distance(self, distance: int):
        """
        Move the robot until the distance to an object is less than or equal to
        the specified value in centimeters.

        This method allows the robot to move forward until the distance
        to an object falls below or equals the specified threshold. The
        distance is measured in centimeters using the robot's sensors.

        :param distance: The maximum distance in centimeters to an object
                        before the robot should stop moving.
        :type distance: int
        :return: None
        Author: Jack McDonald
        """

        self.MotorController.move_forward()
        while self.robot.get_distance() > distance:
            pass
        self.MotorController.stop()

        
    def move_one_tile(self):
        """
        Moves the robot one tile further in the current direction of movement by 
        using the colour sensor to verify that has crossed a black line. 
        This function assumes the robot's movement direction and its environment
        are predefined and does not take any argument.

        :return: None
        """
        # Move forward until black line is detected
        self.move_until_colour("black")

        # Move past the line by specified overrun distance
        self.move_until_distance(OVERRUN_DISTANCE)

    def turn_right(self):
        """
        Executes a right turn operation.
    
        This method turns the robot's chassis to the right by adjusting
        the motor's power and operation. The robot's environment and
        movement are assumed to allow for a smooth turn without obstacles.
        
        :return: None
        """
        self.MotorController.rotate(
            angle=RIGHT,
            speed=self.MotorController.TRN_SPEED
        )
        # Ralph

    def turn_left(self):
        """
        Executes a left turn operation.
    
        This method turns the robot's chassis to the left by adjusting 
        the motor system. Ensure the path is clear before invoking this 
        function to avoid collisions.
        
        :return: None
        """
        self.MotorController.rotate(
            angle=LEFT,
            speed=self.MotorController.TRN_SPEED
        )

        # Ralph

    def turn_around(self):
        """
        Rotates the robot by 180 degrees.
    
        This method enables a complete 180-degree turn for the robot,
        effectively reversing its current direction of travel. This is 
        useful in scenarios where the robot needs to retrace its path.
        
        :return: None
        """
        self.MotorController.rotate(
            angle=AROUND,
            speed=self.MotorController.TRN_SPEED
        )

        # Ralph

    def extinguish_fire(self):
        """
        Activates the fire extinguisher mechanism.
    
        This method is responsible for initiating the robot's fire suppression
        system. Ensure that the fire detection mechanism has identified the 
        fire's location before triggering this function.
        
        :return: None
        """
        # Activate dispenser
        self.MotorController.dispense()

        # Ralph
