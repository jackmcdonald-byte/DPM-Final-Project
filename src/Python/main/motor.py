import time

import math
from math import pi

from project.utils.brick import Motor


class MotorController:
    """
    Handles motor control for a robotic system.

    This class provides functionality for managing and controlling three motors:
    left motor, right motor, and a dispenser motor. It allows the robot to move
    forward, rotate, dispense items, and reset the dispenser to its original position.
    It handles speed and power limits for the motors and converts distances and
    angles into appropriate motor movements.

    :ivar motor_left: The motor controlling the left wheel.
    :type motor_left: Motor
    :ivar motor_right: The motor controlling the right wheel.
    :type motor_right: Motor
    :ivar motor_dispenser: The motor controlling the dispenser mechanism.
    :type motor_dispenser: Motor
    Author: Jack McDonald
    """
    MOTOR_POLL_DELAY = 0.05
    SQUARE_LENGTH = 0.5

    WHEEL_RADIUS = 0.0206  # (meters) Radius of one wheel
    AXLE_LENGTH = 0.0455

    FWD_SPEED = 120  # (deg per sec) Moving forward speed
    TRN_SPEED = 120  # (deg per sec) Turning a corner speed
    DSP_SPEED = 30  # (deg per sec) Dispensing speed

    POWER_LIMIT = 80
    SPEED_LIMIT = 720

    DISTANCE_TO_DEGREES = 180 / (pi * WHEEL_RADIUS)  # scale factor for distance
    ORIENTATION_TO_DEGREES = AXLE_LENGTH / WHEEL_RADIUS  # scale factor for rotation
    DISPENSER_TURN_ANGLE = -62

    MOVEMENT_CORRECTION_FACTOR = 1.15
    LEFT_MOTOR_CORRECTION_FACTOR = 1.00

    def __init__(self):
        """
        Represents a robotic system utilizing three motors: left, right,
        and dispenser. The class initializes these motors with specific
        ports to support motion and dispensing tasks.

        The class encapsulates the setup of its motor components, which
        can be controlled for various operations.

        :Attributes:
            motor_left (Motor): The motor responsible for the left-side
                movement of the robotic system.
            motor_right (Motor): The motor responsible for the right-side
                movement of the robotic system.
            motor_dispenser (Motor): The motor responsible for operating
                the dispenser mechanism of the robotic system.
        Author: Jack McDonald
        """
        self.motor_left = Motor("C")
        self.motor_right = Motor("B")
        self.motor_dispenser = Motor("A")

    def wait_for_motor(self, motor: Motor):
        """
        Waits for a motor to completely stop moving.

        This function continuously checks the current speed of the motor. It first ensures
        that the motor is not already stationary, and if not, it pauses until the motor
        reaches a speed of zero. Afterward, it waits until the motor fully halts to avoid
        any residual motion.

        :param motor: The motor object whose speed will be monitored.
        :type motor: Motor
        Author: Jack McDonald
        """
        while math.isclose(motor.get_speed(), 0):
            time.sleep(self.MOTOR_POLL_DELAY)
        while not math.isclose(motor.get_speed(), 0):
            time.sleep(self.MOTOR_POLL_DELAY)

    def init_motor(self, motor: Motor):
        """
        Initializes the motor by performing necessary setup operations. The method
        resets the motor's encoder, sets power and speed limits, and initializes
        the motor power to zero. Any Input/Output error encountered during these
        operations will be printed.

        :param motor: Instance of the Motor class, representing the motor to
                      initialize.
        :type motor: Motor
        :return: None
        Author: Jack McDonald
        """
        try:
            motor.reset_encoder()
            motor.set_limits(self.POWER_LIMIT, self.SPEED_LIMIT)
            motor.set_power(0)
        except IOError as error:
            print(error)

    def move_distance_forward(self, distance, speed):
        """
        Moves a robot forward for a specified distance at a given speed.

        This function calculates the degrees necessary for the motors to rotate in
        order to move the specified distance forward. It sets the desired speed,
        configures motor limits, and then commands both motors to move relative
        to their current positions. The function ensures that the movement is
        completed by waiting for the right motor to finish its operation.

        :param distance: The distance in units to move forward.
        :type distance: float
        :param speed: The speed in degrees per second for the motors.
        :type speed: int
        :return: None
        Author: Jack McDonald
        """
        try:
            speed *= 2
            self.motor_left.set_dps(speed * self.LEFT_MOTOR_CORRECTION_FACTOR)
            self.motor_right.set_dps(speed)
            self.motor_left.set_limits(self.POWER_LIMIT, speed)
            self.motor_right.set_limits(self.POWER_LIMIT, speed)
            self.motor_left.set_position_relative(int(distance * self.DISTANCE_TO_DEGREES))
            self.motor_right.set_position_relative(int(distance * self.DISTANCE_TO_DEGREES))

            self.wait_for_motor(self.motor_right)
        except IOError as error:
            print(error)

    def rotate(self, angle, speed):
        """
        Performs a rotation by controlling two motors according to the specified angle
        and speed. The method calculates the necessary motor positions based on the
        angle and sets their speeds accordingly. After setting the motor parameters
        and starting the motion, it waits for one motor to complete the rotation.

        :param angle: The rotation angle in degrees, used to determine the relative
                      position change for each motor.
        :type angle: float
        :param speed: The rotational speed in degrees per second to apply to both
                      motors during the rotation.
        :type speed: int
        :return: None
        Author: Jack McDonald
        """
        try:
            self.rotate_no_wait(angle, speed)
            time.sleep(0.5)
            self.wait_for_motor(self.motor_right)
        except IOError as error:
            print(error)

    def rotate_no_wait(self, angle, speed):
        """
        Performs a rotation by controlling two motors according to the specified angle
        and speed. The method calculates the necessary motor positions based on the
        angle and sets their speeds accordingly. After setting the motor parameters
        and starting the motion, it waits for one motor to complete the rotation.

        :param angle: The rotation angle in degrees, used to determine the relative
                      position change for each motor.
        :type angle: float
        :param speed: The rotational speed in degrees per second to apply to both
                      motors during the rotation.
        :type speed: int
        :return: None
        Author: Jack McDonald
        """
        try:
            speed *= 1.5
            angle = angle * self.MOVEMENT_CORRECTION_FACTOR
            self.motor_left.set_dps(speed * self.LEFT_MOTOR_CORRECTION_FACTOR )
            self.motor_right.set_dps(speed)
            self.motor_left.set_limits(self.POWER_LIMIT, speed)
            self.motor_right.set_limits(self.POWER_LIMIT, speed)
            self.motor_left.set_position_relative(int(angle * self.ORIENTATION_TO_DEGREES))
            self.motor_right.set_position_relative(int(-angle * self.ORIENTATION_TO_DEGREES))
        except IOError as error:
            print(error)

    def rotate_to_angle(self, left_motor_angle, right_motor_angle, speed):
        """
        Performs a rotation by controlling two motors according to the specified angle
        and speed. The method calculates the necessary motor positions based on the
        angle and sets their speeds accordingly. After setting the motor parameters
        and starting the motion, it waits for one motor to complete the rotation.

        :param angle: The rotation angle in degrees, used to determine the relative
                      position change for each motor.
        :type angle: float
        :param speed: The rotational speed in degrees per second to apply to both
                      motors during the rotation.
        :type speed: int
        :return: None
        Author: Jack McDonald
        """
        try:
            speed *= 1.5
            self.motor_left.set_dps(speed * self.LEFT_MOTOR_CORRECTION_FACTOR)
            self.motor_right.set_dps(speed)
            self.motor_left.set_limits(self.POWER_LIMIT, speed)
            self.motor_right.set_limits(self.POWER_LIMIT, speed)
            self.motor_left.set_position(left_motor_angle)
            self.motor_right.set_position(right_motor_angle)

            self.wait_for_motor(self.motor_right)
        except IOError as error:
            print(error)

    def dispense(self):
        """
        Controls the operation of dispensing through a motor mechanism.

        This method sets the motor's degree-per-second speed, applies power
        limits, and commands the motor to achieve a relative positional
        movement based on the specified dispenser turn angle. After issuing
        these directives to the motor, it invokes a function to wait for the
        motor operation to complete. If an input/output error occurs during
        the process, the error is caught and printed to the console.

        Author: Jack McDonald
        """
        try:
            self.motor_dispenser.set_dps(self.DSP_SPEED)
            self.motor_dispenser.set_limits(self.POWER_LIMIT, self.DSP_SPEED)
            self.motor_dispenser.set_position_relative(self.DISPENSER_TURN_ANGLE)

            self.wait_for_motor(self.motor_dispenser)
        except IOError as error:
            print(error)

    def reset_dispenser(self):
        """
        Resets the dispenser's motor to its initial state by setting its speed,
        power limits, position, and then waiting for it to stabilize. This is
        useful to ensure the dispenser's motor is prepared for its next operation.

        :return: None
        Author: Jack McDonald
        """
        try:
            self.motor_dispenser.set_dps(self.DSP_SPEED)
            self.motor_dispenser.set_limits(self.POWER_LIMIT, self.DSP_SPEED)
            self.motor_dispenser.set_position(0)

            self.wait_for_motor(self.motor_dispenser)
        except IOError as error:
            print(error)

    def move_forward(self):
        self.motor_left.set_dps(self.FWD_SPEED * self.LEFT_MOTOR_CORRECTION_FACTOR)
        self.motor_right.set_dps(self.FWD_SPEED)
        self.motor_left.set_limits(self.POWER_LIMIT, self.FWD_SPEED)
        self.motor_right.set_limits(self.POWER_LIMIT, self.FWD_SPEED)
        self.motor_left.set_power(20 * self.LEFT_MOTOR_CORRECTION_FACTOR)
        self.motor_right.set_power(20)

    def stop(self):
        self.motor_left.set_power(0)
        self.motor_right.set_power(0)
