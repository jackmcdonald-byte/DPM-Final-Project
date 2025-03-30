from motor import MotorController
import time
from robot import colour_reading

#define constants pertaining to robot turning (in the functions turn_right(), turn_left(), and turn_around())
LEFT = 90 #positive constant for left turn
RIGHT = -90 #negative constant for right turn
AROUND = 180

# Constants for movement tuning
OVERRUN_DISTANCE = 0.05   # meters to move past the line (adjust based on robot size)
TIMEOUT = 5 #timeout constant for one tile forward move

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
    def __init__(self):
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

    def move_until_colour(self, colour: str):
    """
    Moves the robot until the specified colour is detected. The movement stops when the given
    colour is identified. This function assumes a mechanism to detect colours and halts operation
    when the desired condition is fulfilled.

    :param colour: The target colour to be detected during the movement.
    :type colour: str
    :return: None
    """
    # Start moving forward
    self.MotorController.motor_left.set_dps(self.MotorController.FWD_SPEED)
    self.MotorController.motor_right.set_dps(self.MotorController.FWD_SPEED)
    
    # Create timeout variable for safety
    start_time = time.time()
    
    while True:
        current_color = get_colour_name()  
        
        if current_color.lower() == colour.lower():
            print(f"Detected target color {colour} - stopping")
            break
            
        if time.time() - start_time > TIMEOUT:
            self.MotorController.stop()
            raise TimeoutError(f"Color '{colour}' not detected within {TIMEOUT} seconds")
            
        time.sleep(LINE_DETECT_DELAY)
    
    # Stop movement
    self.MotorController.stop()


    def move_until_distance(self, distance: int):
        """
        Move the robot until it covers the specified distance in centimeters.
        
        This method allows the robot to move forward until the specified
        distance is reached. The distance is measured in centimeters and
        converted internally to the units used by the robot's navigation system.
        Ensure that appropriate conditions and validations are set for safe operation.
        
        :param distance: The distance in centimeters the robot should cover 
                        before stopping.
        :type distance: int
        :return: None
        """
        self.MotorController.move_distance_forward(
            distance=distance * self.MotorController.MOVEMENT_CORRECTION_FACTOR,
            speed=self.MotorController.FWD_SPEED
        )
        #Ralph

    def move_one_tile(self):
    """
    Moves the robot one tile further by detecting and crossing a black line.
    
    :return: None
    :raises TimeoutError: If line isn't detected within reasonable time
    """        
   try:
        # Move forward until black line is detected
        self.move_until_colour("black")
        
        # Move past the line by specified overrun distance
        self.move_until_distance(OVERRUN_DISTANCE)  

    except Exception as e:
        self.MotorController.stop()
        raise
            
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
        #Ralph

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

        #Ralph

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

        #Ralph

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
        
        #Ralph
