#k-squared 
from utils import sound
from utils.brick import TouchSensor, EV3ColorSensor, wait_ready_sensors, reset_brick
from time import sleep
import math

# Constants
DELAY_SEC = 0.01  # Delay between measurements
TOUCH_SENSOR = TouchSensor(4)  # Touch sensor on port 1
COLOR_SENSOR = EV3ColorSensor(2)  # Color sensor on port 2

# Predefined mean normalized RGB values for each block color
COLOR_DATA = {
    "red": {"R": 0.6951, "G": 0.2053, "B": 0.0996},
    "blue": {"R": 0.1771, "G": 0.4486, "B": 0.3743},
    "green": {"R": 0.3946, "G": 0.5585, "B": 0.0469},  # Updated green values
    "orange": {"R": 0.6921, "G": 0.2253, "B": 0.0826},
    "yellow": {"R": 0.4914, "G": 0.4774, "B": 0.0313},
    "purple": {"R": 0.3972, "G": 0.3165, "B": 0.2863},
    "white": {"R": 0.4158, "G": 0.4032, "B": 0.1810},  # Updated white values
    "black": {"R": 0.3980, "G": 0.4418, "B": 0.1602},  # Updated black values
}

def normalize_rgb(raw_r, raw_g, raw_b):
    """Normalize raw RGB values to the range [0, 1]."""
    total = raw_r + raw_g + raw_b
    if total == 0:  # Avoid division by zero
        return 0, 0, 0
    return raw_r / total, raw_g / total, raw_b / total

def calculate_k_squared(normalized_rgb, color_data):
    """Calculate squared Euclidean distance between RGB values."""
    distances = {}
    for color, values in color_data.items():
        distance = (
            (normalized_rgb[0] - values["R"])**2 +
            (normalized_rgb[1] - values["G"])**2 +
            (normalized_rgb[2] - values["B"])**2
        )
        distances[color] = distance
    return distances

def identify_color(distances):
    """Identify the color with the smallest distance."""
    return min(distances, key=distances.get)

def main():
    wait_ready_sensors(True)
    print("Sensors are ready. Press the touch sensor to measure color.")

    try:
        while True:
            if TOUCH_SENSOR.is_pressed():
                color_data = COLOR_SENSOR.get_value()
                if color_data is None:
                    print("error try again")
                    continue
                raw_r, raw_g, raw_b = color_data[:3]
                
                print(f"Raw RGB values: R={raw_r}, G={raw_g}, B={raw_b}")
                
                normalized_rgb = normalize_rgb(raw_r, raw_g, raw_b)
                print(f"Normalized RGB values: {normalized_rgb}")
                
                distances = calculate_k_squared(normalized_rgb, COLOR_DATA)
                identified_color = identify_color(distances)
                
                print(f"Identified color: {identified_color}")
 # Beep to indicate the color is identified
                
                sleep(DELAY_SEC)  # Avoid multiple detections for a single press
    except KeyboardInterrupt:
        print("Exiting program.")
    finally:
        reset_brick()

if __name__ == "__main__":
    main()