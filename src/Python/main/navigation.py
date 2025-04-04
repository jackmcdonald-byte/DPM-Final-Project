import time
from chassis import Chassis
from motor import MotorController

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
    def __init__(self, robot, motor_controller: MotorController, chassis: Chassis):
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
        self.blocked = None
        self.search_array = [
            ['u', 'u', 'u'],
            ['u', 'u', 'u'],
            ['w', 'c', 'w']
        ]
        self.search_queue = []
        self.found = 0
        self.motor = motor_controller
        self.robot = robot
        self.chassis = chassis

    def sweep(self):
        left_start_pos = self.motor.motor_left.get_position()
        right_start_pos = self.motor.motor_right.get_position()

        self.motor.rotate(angle=90, speed=self.motor.TRN_SPEED)
        self.motor.rotate_no_wait(angle=-180, speed=self.motor.TRN_SPEED/3)
        time.sleep(0.2)
        end_time = time.time() + 5
        while time.time() < end_time:   
            if self.robot.get_colour() == "red":
                time.sleep(5)
                self.motor.stop()
                self.chassis.extinguish_fire()
                self.found += 1
            #elif self.robot.get_colour() == "green":
                #self.blocked = True
        self.motor.rotate_to_angle(left_motor_angle=left_start_pos,
                                   right_motor_angle=right_start_pos,
                                   speed=self.motor.TRN_SPEED)


