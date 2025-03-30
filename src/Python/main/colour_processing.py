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
        "red": [0.6951, 0.2053, 0.0996],
        "blue": [0.1771, 0.4486, 0.3743],
        "green": [0.3946, 0.5585, 0.0469],
        "orange": [0.6921, 0.2253, 0.0826],
        "yellow": [0.4914, 0.4774, 0.0313],
        "purple": [0.3972, 0.3165, 0.2863],
        "white": [0.4158, 0.4032, 0.1810],
        "black": [0.3980, 0.4418, 0.1602],
        }
    #RALPH

    def _calculate_distance(self, color1, color2):
        """
        Calculate squared Euclidean distance between two RGB colors.
        """
        return sum((a - b) ** 2 for a, b in zip(color1, color2))
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

