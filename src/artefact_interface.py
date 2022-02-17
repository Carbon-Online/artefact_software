import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib
import vlc
import time

class Artefact:
    """
    The artefact class is for describing and updating the state of the
    artefact.
    """

    def __init__(self, gpio_pins_motor, path_to_audio):
        #: The source gpio pins the motor is connected to
        self.motor_pins = gpio_pins_motor
        #: Path to the played audio file
        self.audio_file = path_to_audio
        #: Current position of the motor
        self.current_position = 850
        #: Bool for ensuring just one warning for 10 percent
        # left
        self.not_warned_10_percent = True
        #: Bool for ensuring just one warning for budget
        # used up
        self.not_warned_used_up = True

    def update(self, step_number):
        """
        Updates the artefact by calling the according update methods for changing
        the position of the motor and in case the remaining budget - the motor has
        turned 15 times - is 0 or just 10% percent left a sound is played.

        :param step_number: int describing how many steps to turn
        """
        # updates motor position (artefact shrinking)
        self.update_position(step_number)
        # warning sound if just 10% of the budget left
        if self.current_position <= 85 and self.not_warned_10_percent:
            self.make_sound()
            self.not_warned_10_percent = False
        # warning sound  if budget us used up
        if self.current_position <= 0 and self.not_warned_used_up:
            self.make_sound()
            self.make_sound()
            self.current_position = 0
            self.not_warned_used_up = False

    def update_position(self, step_number, moving_down=True):
        """
        Updates the artefact motor by changing the position of the motor
        and adapts the current position.

        :param step_number: int describing how many steps to turn
        :param moving_down: bool indicating the direction change of the 
        artefacts state
        """
        if self.current_position - step_number < 0:
            step_number = self.current_position
        motor = RpiMotorLib.BYJMotor("MyMotorOne", "Nema")
        time.sleep(0.5)
        motor.motor_run(self.motor_pins, 
                        0.001, 
                        step_number, 
                        moving_down, 
                        False, 
                        "full", 
                        .05)
        GPIO.cleanup()
        if moving_down:
            self.current_position -= step_number

    def reset(self):
        """
        Resets the artefact motor by changing the position of the motor
        and resets the current position to zero.
        """
        step_size = 850 - self.current_position
        self.current_position = 850
        self.update_position(step_size, False)
        self.not_warned_10_percent = True
        self.not_warned_used_up = True

    def make_sound(self):
        """
        Plays a mp3 audio file via a speaker.
        """
        p = vlc.MediaPlayer(self.audio_file)
        p.play()
