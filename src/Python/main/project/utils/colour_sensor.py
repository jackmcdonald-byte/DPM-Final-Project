from brick import EV3ColorSensor, wait_ready_sensors

COLOUR_SENSOR = EV3ColorSensor(2)
wait_ready_sensors()


def get_raw_rgb() -> list[float]:
    """
    Retrieves the current raw RGB values from the color sensor.

    This function calls a specific method on the color sensor object to fetch
    the most recent raw RGB values in a list.

    :return: A list containing the red, green, and blue component values as
        floating-point numbers.
    :rtype: list[float]
    Author: Jack McDonald
    """
    return COLOUR_SENSOR.get_rgb()


def get_normalized_rgb() -> list[float]:
    """
    Calculates and returns the normalized RGB values as a list of floats. The
    resulting values represent the proportion of each RGB component in relation
    to the total of the first three components in the raw RGB input. If the sum
    of the first three components of the raw RGB is zero, the function avoids
    division by zero and returns a list with all components set to zero.

    :return: A list of three floats representing the normalized RGB values. Each
        component is the proportion of the corresponding RGB value relative to
        the total of the first three components. If the total is zero, a list of
        `[0, 0, 0]` is returned.
    :rtype: list[float]
    Author: Jack McDonald
    """
    raw_rgb = get_raw_rgb()
    total = sum(raw_rgb[:3])
    if total == 0:
        return [0, 0, 0]
    return [raw_rgb[0] / total, raw_rgb[1] / total, raw_rgb[2] / total]
