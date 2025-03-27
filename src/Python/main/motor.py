import time
from project.utils.brick import Motor, BP
import math
from math import pi

MOTOR_LEFT = Motor("C")
MOTOR_RIGHT = Motor("B")
MOTOR_DISPENSER = Motor("A")

MOTOR_POLL_DELAY = 0.05
SQUARE_LENGTH = 0.5

WHEEL_RADIUS = 0.0206 # (meters) Radius of one wheel
AXLE_LENGTH = 0.0455

FWD_SPEED = 100  # (deg per sec) Moving forward speed
TRN_SPEED = 180  # (deg per sec) Turning a corner speed
DSP_SPEED = 30   # (deg per sec) Dispensing speed

POWER_LIMIT = 80
SPEED_LIMIT = 720

DISTANCE_TO_DEGREES = 180 / (pi * WHEEL_RADIUS)  # scale factor for distance
ORIENTATION_TO_DEGREES = AXLE_LENGTH / WHEEL_RADIUS  # scale factor for rotation
DISPENSER_TURN_ANGLE = -47

MOVEMENT_CORRECTION_FACTOR = 1

def wait_for_motor(motor: Motor):
    while math.isclose(motor.get_speed(), 0):
        time.sleep(MOTOR_POLL_DELAY)
    while not math.isclose(motor.get_speed(), 0):
        time.sleep(MOTOR_POLL_DELAY)


def init_motor(motor: Motor):
    try:
        motor.reset_encoder()
        motor.set_limits(POWER_LIMIT, SPEED_LIMIT)
        motor.set_power(0)
    except IOError as error:
        print(error)


def move_distance_forward(distance, speed):
    try:
        MOTOR_LEFT.set_dps(speed)
        MOTOR_RIGHT.set_dps(speed)
        MOTOR_LEFT.set_limits(POWER_LIMIT, speed)
        MOTOR_RIGHT.set_limits(POWER_LIMIT, speed)
        MOTOR_LEFT.set_position_relative(int(distance * DISTANCE_TO_DEGREES))
        MOTOR_RIGHT.set_position_relative(int(distance * DISTANCE_TO_DEGREES))

        wait_for_motor(MOTOR_RIGHT)
    except IOError as error:
        print(error)


def rotate(angle, speed):
    try:
        MOTOR_LEFT.set_dps(speed)
        MOTOR_RIGHT.set_dps(speed)
        MOTOR_LEFT.set_limits(POWER_LIMIT, speed)
        MOTOR_RIGHT.set_limits(POWER_LIMIT, speed)
        MOTOR_LEFT.set_position_relative(int(angle * ORIENTATION_TO_DEGREES))
        MOTOR_RIGHT.set_position_relative(int(-angle * ORIENTATION_TO_DEGREES))

        wait_for_motor(MOTOR_RIGHT)
    except IOError as error:
        print(error)


def dispense():
    try:
        MOTOR_DISPENSER.set_dps(DSP_SPEED)
        MOTOR_DISPENSER.set_limits(POWER_LIMIT, DSP_SPEED)
        MOTOR_DISPENSER.set_position_relative(DISPENSER_TURN_ANGLE)

        wait_for_motor(MOTOR_DISPENSER)
    except IOError as error:
        print(error)


def reset_dispenser():
    try:
        MOTOR_DISPENSER.set_dps(DSP_SPEED)
        MOTOR_DISPENSER.set_limits(POWER_LIMIT, DSP_SPEED)
        MOTOR_DISPENSER.set_position(0)

        wait_for_motor(MOTOR_DISPENSER)
    except IOError as error:
        print(error)