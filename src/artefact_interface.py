from RpiMotorLib import RpiMotorLib
import RPi.GPIO as GPIO
import math
import vlc


class Artefact:
    """
    The artefact class is for describing and updating the state of the
    artefact.
    """

    def __init__(self, gpio_pins_motor, path_to_audio):
        #: The source gpio pin the motor is connected to
        self.motor_pins = gpio_pin_motors
        #: Path to the played audio file
        self.audio_file = path_to_audio
        #: Initializing of the connection to the motor
        self.motor = self.init_motor()
        #: Current position of the motor
        self.current_position = 0  
        #: Bool for ensuring just one warning for 10 percent
        # left
        self.not_warned_10_percent = True
        #: Bool for ensuring just one warning for budget
        # used up
        self.not_warned_used_up = True

    def init_motor(self):
        """
        Initializes the GPIO pins and connects the raspberry pi with
        the motor. Turns motor to the start position.

        :return: A PWM instance
        """
        motor = RpiMotorLib.BYJMotor("MyMotorOne", "Nema") # GPIO motor_pin als PWM mit 50Hz
        return motor

    def update(self, step_number):
        """
        Updates the artefact by calling the according update methods for changing
        the position of the motor and in case the remaining budget - the motor has
        turned 15 times - is 0 or just 10% percent left a sound is played.

        :param step_number: int describing how many steps to turn
        """
        # updates motor position (artefact shrinking)
        self.update_position(steps)
        # warning sound if just 10% of the budget left
        if self.current_position <= 380 & self.not_warned_10_percent:
            self.make_sound()
            self.not_warned_10_percent = False
        # warning sound  if budget us used up
        if self.current_position <= 0 & self.not_warned_10_percent:
            self.make_sound()
            self.make_sound()
            self.current_position = 0
            self.not_warned_used_up = False

    def update_position(self, step_number, ccwise=True):
        """
        Updates the artefact motor by changing the position of the motor
        and adapts the current postion.

        :param step_number: int describing how many steps to turn
        """
	if self.current_position - step_number < 0:
            step_number = self.current_position
        self.motor.motor_run(self.motor_pins, steps=step_number, steptype="full", ccwise=ccwise) 
        self.current_position -= step_number

    def reset(self):
        """
        Resets the artefact motor by changing the position of the motor
        and resets the current position to zero.
        """
        self.update_position(3800 - self.current_position, False)
        self.current_position = 3800 
        self.not_warned_10_percent = True
        self.not_warned_used_up = True

    def make_sound(self):
        """
        Plays a mp3 audio file via a speaker.
        """
        p = vlc.MediaPlayer(self.audio_file)
        p.play()
