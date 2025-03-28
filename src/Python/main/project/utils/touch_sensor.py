from brick import TouchSensor, wait_ready_sensors

TOUCH_SENSOR = TouchSensor(1)
wait_ready_sensors()


def is_pressed() -> bool:
    """
    Determine if a specific sensor is pressed.

    Parameters:
    sensor (int): The identifier of the sensor to check. Accepted values are
    1 for TOUCH_SENSOR_1 and 2 for TOUCH_SENSOR_2.

    Returns:
    bool: True if the specified sensor is pressed, False otherwise.
    """
    return TOUCH_SENSOR.is_pressed()