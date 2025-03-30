import colour_processing
from project.utils.touch_sensor import is_pressed
from project.utils.us_sensor import get_distance
from project.utils.colour_sensor import get_normalized_rgb, get_raw_rgb

class SensorController:
    """
    Controls and interfaces with various sensors.

    This class is designed to handle the interaction with touch, color, and
    ultrasonic sensors. It provides methods to obtain sensor states and
    measurements, supporting the integration of these sensors into larger
    applications.

    :ivar touch_sensor: Represents the touch sensor connected to the system.
    :type touch_sensor: Optional[Any]
    :ivar colour_sensor: Represents the color sensor connected to the system.
    :type colour_sensor: Optional[Any]
    :ivar us_sensor: Represents the ultrasonic sensor connected to the system.
    :type us_sensor: Optional[Any]
    Author: Jack McDonald
    """
    def __init__(self):
        """
        Represents an initialization of sensor attributes for an object.

        This class defines and initializes three key sensor attributes: a touch sensor,
        a colour sensor, and an ultrasonic sensor, all of which are pivotal for various
        operations involving object interaction and detection.

        Attributes:
            touch_sensor:
                A placeholder for the touch sensor associated with the object.
            colour_sensor:
                A placeholder for the colour sensor associated with the object.
            us_sensor:
                A placeholder for the ultrasonic sensor associated with the object.
        Author: Jack McDonald
        """
        self.touch_sensor = None
        self.colour_sensor = None
        self.us_sensor = None

    def get_colour_name(self):
        """
        Represents a method that retrieves the name of a color.

        The `get_colour_name` method accesses an internal mechanism or a
        specific procedure to extract the name of a color, presumably
        represented or identified within the instance calling the method. It
        aims to provide a human-readable or standard representation of the
        associated color.

        :return: The name of the color as a string.
        :rtype: str
        Author: Jack McDonald
        """
        normalized_rgb = get_normalized_rgb()
        processor = colour_processing.ColourProcessing()
        return processor.identify_colour(normalized_rgb)
        #RALPH

    def __get_colour_raw(self):
        """
        Fetches and returns the raw color data in its original form without
        any processing or conversion.

        :return: Raw color data
        :rtype: Any
        Author: Jack McDonald
        """
        return get_raw_rgb()

    def get_touch_sensor_state(self):
        """
        Retrieves the current state of the touch sensor.

        This method queries the status of the touch sensor and determines its
        current state, typically whether it is being touched or not.

        :return: The state of the touch sensor, typically a boolean where `True`
            indicates the sensor is being touched and `False` indicates it is not.
        :rtype: bool
        Author: Jack McDonald
        """
        return is_pressed()

    def get_us_sensor_distance(self):
        """
        Retrieves the ultrasonic sensor distance measurement to determine the proximity of an object.

        This function interacts with the ultrasonic sensor to obtain distance values, typically
        used in applications such as obstacle detection, navigation, or measurement tasks.

        :return: The distance value, as measured by the ultrasonic sensor.
        :rtype: float
        Author: Jack McDonald
        """
        return get_distance()
