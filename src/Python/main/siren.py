from pygame import mixer

SIREN_MP3 = "src/Python/main/project/mp3/fire-truck-siren-307510.mp3"

class Siren:
    """
    Class representing a Siren functionality.

    The Siren class is designed to manage the operation of a siren system. It provides
    functionalities to play and stop the siren. This class can be used in applications
    where audible signaling is required.

    :ivar is_active: Indicates whether the siren is currently active.
    :type is_active: bool

    Author: Jack McDonald
    """

    def __init__(self):
        """
        A class representing an example entity with an activation state.

        This class is used to manage an activation state defined by the `is_active`
        attribute. It provides initial setup for the activation property during the
        creation of the instance.

        Author: Jack McDonald
        """
        self.is_active = False
        mixer.init()

    def play_siren(self):
        """
        Plays a siren sound.

        This method activates a siren or alarm sound mechanism. The purpose of this
        method is to simulate or trigger a siren sound in an application or system.
        The specific sound details or implementation are not described here and need
        to be handled in the method's internal logic.

        :return: None

        Author: Jack McDonald
        """
        if not self.is_active:
            try:
                self.sound = mixer.Sound(SIREN_MP3)
                self.sound.play(loops=-1)  # -1 for infinite loops
                self.is_active = True
            except Exception as e:
                print(f"Error playing siren: {e}")
                self.is_active = False

    def stop_siren(self):
        """
        Stops the currently active siren.

        This method triggers an operation to cease the activity of a running siren. It
        doesn't return any value or raise an error upon execution.

        :return: None

        Author: Jack McDonald
        """
        if self.is_active:
            mixer.stop()  # Stop all mixer playback
            self.is_active = False
