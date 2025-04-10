import time

from Python.main.chassis import Chassis
from motor import MotorController


class Navigation:
    """
    Represents a navigation system for searching a 2D grid with different 
    states like unsearched areas, walls, furniture, current position, and 
    searched areas.
    
    The Navigation class initializes the search grid and provides methods 
    that can be used to navigate, update positions, and determine the next 
    route. It maintains a queue for search operations, tracks the 
    number of fires found, and facilitates obstacle detection using 
    sensory data.

    :ivar found: The count of fires detected and extinguished during the search.
    :type found: int
    :ivar blocked: A boolean that indicates whether an obstacle (green) is 
        detected during operation, restricting further movement.
    :type blocked: bool or None
    :ivar sweep_angle: The angle (in degrees) the robot rotates during the 
        sweeping operation when scanning for obstacles and fires.
    :type sweep_angle: int
    Author: Jack McDonald
    """

    def __init__(self, robot, motor_controller: MotorController, chassis: Chassis):
        """
        Initializes the Navigation class for grid-based search operations, 
        incorporating robot movement, obstacle detection, and fire 
        extinguishing logic.
    
        :param robot: The robot instance used for navigation and sensory 
            operations, such as detecting colors.
        :param motor_controller: An instance of MotorController managing 
            wheel rotations and movement during navigation and fire 
            extinguishing.
        :param chassis: The Chassis object responsible for robot actions 
            like fire extinguishing and maintaining movement.
    
        :Attributes:
            blocked (bool or None): Indicates whether an obstacle is detected, 
                preventing further movement.
            found (int): Tracks the total number of fires detected and handled.
            motor (MotorController): Handles tasks such as movement, rotation, 
                and position restoration.
            robot: The robot performing navigation and sensory interactions.
            chassis (Chassis): Handles fire extinguishing and other 
                robot movement-related actions.
            sweep_angle (int): Controls how far the robot rotates during 
                a sweeping action to detect obstacles or fires.
        """
        self.blocked = None
        self.found = 0
        self.motor = motor_controller
        self.robot = robot
        self.chassis = chassis
        self.sweep_angle = 120  # The angle (in degrees) for rotational sweeping when the robot scans for fires or obstacles.

    def sweep(self):
        """
        Performs a rotational sweep to scan for obstacles or fires using 
        the robot's sensors. The robot rotates, detects colors, and takes 
        appropriate actions like extinguishing fires or marking pathways as blocked.
    
        :Steps:
            1. Records the initial wheel positions.
            2. Rotates the robot over half the sweep angle, initiating a subsequent 
                rotation to cover the entire angle.
            3. If the color sensor detects 'red' (fire), stops the motion, extinguishes 
                the fire, and increments the fire count.
            4. If the color sensor detects 'green' (obstacle), updates the `blocked` 
                attribute to True.
            5. Restores the wheel positions after the sweep is completed.
    
        :Attributes Used or Updated:
            blocked: Set to True if a green obstacle is detected.
            found: Incremented when a fire is detected and extinguished.
    
        :Return: None
        """
        left_start_pos = self.motor.motor_left.get_position()
        right_start_pos = self.motor.motor_right.get_position()

        self.motor.rotate(angle=self.sweep_angle / 2, speed=self.motor.TRN_SPEED)
        # time.sleep(0.1)
        self.motor.rotate_no_wait(angle=self.sweep_angle * -1, speed=self.motor.TRN_SPEED / 1.125)
        end_time = time.time() + 1.7
        while time.time() < end_time:
            if self.robot.get_colour() == "red":
                self.motor.stop()
                self.chassis.extinguish_fire()
                self.found += 1
                break
            elif self.robot.get_colour() == "green":
                self.blocked = True
        self.motor.rotate_to_angle(left_motor_angle=left_start_pos,
                                   right_motor_angle=right_start_pos,
                                   speed=self.motor.TRN_SPEED)
        time.sleep(0.2)
