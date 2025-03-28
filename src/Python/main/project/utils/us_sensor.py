from typing import Type

from brick import EV3UltrasonicSensor, wait_ready_sensors

us_sensor = EV3UltrasonicSensor(3)
wait_ready_sensors()


def get_distance() -> int:
    """
    Returns the distance measured by an ultrasonic sensor in centimeters.

    Returns:
        int: The distance measured by the ultrasonic sensor in centimeters.
    """
    return int(us_sensor.get_value())