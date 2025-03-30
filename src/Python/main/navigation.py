class Navigation:
    """
    Represents a navigation system for searching a 2D grid with different 
    states like unsearched areas, walls, furniture, current position, and 
    searched areas.

    The Navigation class initializes the search grid and provides methods 
    that can be used to explore, update positions, and determine the next 
    route. It maintains a queue for search operations and tracks the 
    number of found fires.

    :ivar search_array: A 2D list representing the search grid. Each cell 
        can contain values ('u' for unsearched, 'w' for wall, 'f' for 
        furniture, 'c' for current position, 's' for searched).
    :type search_array: list[list[str]]
    :ivar search_queue: A list representing the queue used to store 
        search operations.
    :type search_queue: list
    :ivar found: The count of fires found during the search.
    :type found: int
    Author: Jack McDonald
    """
    def __init__(self):
        """
        Class responsible for managing a search operation in a grid-like structure. The 
        class keeps track of the search state and dynamically updates based on the 
        search progress. The grid elements can represent different states of the 
        search using predefined symbols.

        :Attributes:
            search_array: list of list of str
                A 2D grid representing the search area. Each cell in the grid can take 
                values such as 'u' (unsearched), 'w' (wall), 'f' (furniture), 'c' 
                (current position), or 's' (searched) to depict the current state of 
                the search area.
            search_queue: dict
                A list used to keep track of the positions to be searched or 
                actively being processed during the search operation.
            found: int
                A counter representing the number of fires found during the search.
        """
        # u = unsearched
        # w = wall
        # f = furniture
        # c = current pos.
        # s = searched
        self.search_array = [
            ['u', 'u', 'u'],
            ['u', 'u', 'u'],
            ['w', 'c', 'w']
        ]
        self.search_queue = []
        self.found = 0

    def __queue_search(self):
        """
        Represents a private method for adding all unsearched tiles 
        to the search queue.
        
        This function iterates through the search grid and identifies 
        all tiles marked as 'u' (unsearched). Each identified tile's 
        position is added to the search queue for further processing.
        
        :return: None
        :rtype: None
        Author: Jack McDonald
        """
        pass

    def get_next_route(self):
        """
        Handles the computation and retrieval of the next route in a series of routes.
        This method is intended to provide navigation functionality by determining
        and returning the next logical route from a defined set or sequence.

        :return: The next route determined by the calculation or retrieval.
        :rtype: str
        Author: Jack McDonald
        """
        pass

    def update_position(self):
        """
        Updates the position of the robot. This method should calculate and set the
        new position based on the relevant properties or parameters of the object.
        It is designed to handle any internal logic needed to properly update the
        position attribute or state.

        :return: None
        :rtype: NoneType
        Author: Jack McDonald
        """
        pass