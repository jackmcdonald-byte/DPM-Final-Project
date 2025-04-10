class ColourProcessing:
    """
    A utility class for processing and analyzing colour data.
    
    This class provides functionality to determine the closest matching 
    colour from a predefined set of reference colours based on RGB values. 
    It is designed for applications requiring colour recognition or analysis.
    
    Author: Jack McDonald
    """
    def __init__(self):
        # Predefined color reference data (normalized RGB)
        self.COLOR_REF = {
            "black": [8.53, 9.47, 3.47],
            "grey": [199, 155, 17],
            "green": [125.60, 177.80, 14.93],
            "orange": [214.40, 75.67, 13.60],
            "purple": [90.87, 48.13, 42.20],
            "red": [161.33, 17.47, 7.93],
            "white": [250.00, 242.40, 108.80],
            "yellow": [277.53, 237.00, 22.20],
        }

    def _calculate_distance(self, color1, color2):
        """
        Calculate the Euclidean distance between two RGB colors.
        
        This method is used to measure the similarity between a given colour 
        and reference colours by calculating the geometric distance.
        """
        return ((color1[0] - color2[0]) ** 2 + (color1[1] - color2[1]) ** 2 + (color1[2] - color2[2]) ** 2) ** 0.5

    def identify_colour(self, colour: list):
        """
        Identify the closest matching colour from a predefined reference set.
        
        This function compares the provided RGB colour with a set of reference 
        colours and returns the name of the closest match based on minimum 
        Euclidean distance.

        :param colour: A list of three RGB values (red, green, blue) to 
                       match against the reference colours.
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

