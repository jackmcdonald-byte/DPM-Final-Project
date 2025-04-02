from project.utils.brick import TouchSensor, wait_ready_sensors

TOUCH_SENSOR = TouchSensor(4)
wait_ready_sensors()


def is_pressed() -> bool:
    """
    Checks the state of the touch sensor and returns whether it is pressed.

    This function interacts with the touch sensor to determine if it is currently
    being pressed. The function returns a boolean indicating the state of the
    touch sensor.

    :return: Boolean value indicating the state of the touch sensor. True if the
        sensor is pressed, otherwise False.
    :rtype: bool
    Author: Jack McDonald
    """
    return TOUCH_SENSOR.is_pressed()