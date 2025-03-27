from chassis import Chassis
from extinguisher import Extinguisher
from navigation import Navigation
from sensors import SensorController
from siren import Siren

import colour_processing


class Robot:

    def __init__(self):
        self.state = "idle"
        self.chassis = Chassis()
        self.extinguisher = Extinguisher()
        self.navigation = Navigation()
        self.sensors = SensorController()
        self.siren = Siren()
        self.__create_threads()

    def run(self):
        input("Press Enter to begin...")
        try:
            self.__transition_to("NavigationA")
            self.__enter_navigation_a()

            self.__transition_to("Search")
            self.__enter_search()

            self.__transition_to("NavigationB")
            self.__enter_navigation_b()
        except IOError as error:
            print(error)


    def stop(self):
        try:
            self.__transition_to("idle")
        except IOError as error:
            print(error)


    def __transition_to(self, new_state: str) -> None:
        self.__exit_state()
        self.state = new_state
        self.__enter_state()

    def __exit_state(self) -> None:
        if self.state == "NavigationA":
            self.siren.stop_siren()

    def __enter_state(self) -> None:
        if self.state == "NavigationA":
            self.siren.play_siren()
        if self.state == "idle":
            # TODO Stop all robot functions here
            pass

    def __create_threads(self):
        pass

    def __enter_navigation_a(self):
        pass

    def __enter_search(self):
        pass

    def __enter_navigation_b(self):
        pass
