from project.utils.brick import EV3UltrasonicSensor, wait_ready_sensors

us_sensor = EV3UltrasonicSensor(1)
wait_ready_sensors()


def get_distance() -> int:
    """
    Calculates the distance measured by the ultrasonic sensor.
    
    This function retrieves the current value from the ultrasonic sensor in 
    centimeters and returns it as an integer, representing the distance.
    
    :return: Distance measured by the ultrasonic sensor in centimeters.
    :rtype: int
    Author: Jack McDonald
    """
    return int(us_sensor.get_value())
