class ColourProcessing:
    """
    Processes and analyzes colour data for determining dominant colours.

    This class provides functionality to process and analyze colour data
    for various applications, including identifying the dominant colour
    in a given dataset.

    Author: Jack McDonald
    """
    def __init__(self):
        # Predefined color reference data (normalized RGB)
        self.COLOR_REF = {
            "black": [8.53, 9.47, 3.47],
            "black": [40, 40, 15],
            "black": [17, 22, 6],
            "grey": [60, 60, 20],
            "grey": [94, 52, 46],
            "grey": [86, 44, 38],
            "grey": [80, 84, 31],
            "green": [125.60, 177.80, 14.93],
            "orange": [214.40, 75.67, 13.60],
            "purple": [90.87, 48.13, 42.20],
            "red": [161.33, 17.47, 7.93],
            "white": [250.00, 242.40, 108.80],
            "yellow": [277.53, 237.00, 22.20],
        }
        #RALPH

    def _calculate_distance(self, color1, color2):
        """
        Calculate squared Euclidean distance between two RGB colors.
        """
        return ((color1[0] - color2[0]) ** 2 + (color1[1] - color2[1]) ** 2 + (color1[2] - color2[2]) ** 2) ** 0.5
    #RALPH

    def identify_colour(self, colour: list):
        """
        Identify the dominant colour in a given list of colour values.

        This function analyzes the provided list of normalized colour values and determines
        the dominant or most prominent colour. It serves as a utility for
        processing colour-related data.

        :param colour: A list of RGB values to be analyzed.
        :type colour: list
        :return: The dominant colour determined from the analysis.
        :rtype: str
        Author: Jack McDonald
        """
        if not colour or len(colour) != 3:
            return "unknown"
            
        # Calculate distances to all reference colors
        distances = {
            color_name: self._calculate_distance(colour, ref_rgb)
            for color_name, ref_rgb in self.COLOR_REF.items()
        }
        
        # Return the color with smallest distance
        return min(distances.items(), key=lambda x: x[1])[0]
    #RALPH

