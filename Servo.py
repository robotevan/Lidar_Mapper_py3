import pigpio
import time

SERVO_PIN = 18


class Servo:
    def __init__(self):
        """
        SERVO MUST BE ATTACHED TO PIN 18, this is the only pin with PWM
        """
        self.pi = pigpio.pi()
        self.pi.set_mode(SERVO_PIN, pigpio.OUTPUT)
        self.angle = 90  # start angle at 90 degrees
        self.set_angle(90)  # Set servos value to 90 degrees

    def set_angle(self, angle):
        """
        Set the servos angle
        :param angle: angle between 0 and 180
        """
        self.angle = angle
        # The function below was obtined by fitting a angle/pulse width curve width (3rd order polynomial)
        pulse_width = (-1.4631915866*10**-4)*(angle**3) + (5.361552028*10**-2)*(angle**2) + 6.2010582011*(angle) + 500
        # pigpio allows up to 2500 microsecond pulse, cap at this val, min val supported by pigpio is 500!
        if pulse_width > 2500:
            pulse_width = 2500
        self.pi.set_servo_pulsewidth(18, pulse_width)

    def read_angle(self):
        return self.angle


