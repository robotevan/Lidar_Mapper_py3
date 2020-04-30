import RPi.GPIO as GPIO
import time


MS1 = 12
MS2 = 16
MS3 = 21
STEP_PIN = 26
DIR_PIN = 20
STEP_ANGLE = 1.8

class Stepper:
    def __init__(self, step_mode=1, step_direction=0):
        self. angle = 0  # Current angle of the stepper
        # layout setup
        GPIO.setmode(GPIO.BCM)

        # Setup three pins used to set step size
        GPIO.setup(MS1, GPIO.OUT)
        GPIO.setup(MS2, GPIO.OUT)
        GPIO.setup(MS3, GPIO.OUT)

        # Setup Direction and Step pins
        GPIO.setup(STEP_PIN,  GPIO.OUT)
        GPIO.setup(DIR_PIN, GPIO.OUT)

        # Configure step direction
        self.step_direction = step_direction  # 0=cw, 1 =ccw
        self.set_direction(step_direction)  # Set pins for direction

        self.step_size = STEP_ANGLE
        self.step_mode = step_mode  # 1=full, 2=half, 3=quarter, 4=eighth, 5=sixteenth
        self.set_step_size(step_mode)  # Set pins for step size

    def set_step_size(self, mode):
        """
        Set the size of each step
        :param mode: int between 1 and 5
        :return:
        """
        if mode == 1:
            self.step_size = STEP_ANGLE
            GPIO.output(MS1, GPIO.LOW)
            GPIO.output(MS2, GPIO.LOW)
            GPIO.output(MS3, GPIO.LOW)
        elif mode == 2:
            self.step_size = STEP_ANGLE / 2
            GPIO.output(MS1, GPIO.HIGH)
            GPIO.output(MS2, GPIO.LOW)
            GPIO.output(MS3, GPIO.LOW)
        elif mode == 3:
            self.step_size = STEP_ANGLE / 4
            GPIO.output(MS1, GPIO.LOW)
            GPIO.output(MS2, GPIO.HIGH)
            GPIO.output(MS3, GPIO.LOW)
        elif mode == 4:
            self.step_size = STEP_ANGLE / 8
            GPIO.output(MS1, GPIO.HIGH)
            GPIO.output(MS2, GPIO.HIGH)
            GPIO.output(MS3, GPIO.LOW)
        elif mode == 5:
            self.step_size = STEP_ANGLE / 16
            GPIO.output(MS1, GPIO.HIGH)
            GPIO.output(MS2, GPIO.HIGH)
            GPIO.output(MS3, GPIO.HIGH)
        self.step_mode = mode

    def set_direction(self, step_dir):
        if step_dir == 0:
            self.step_direction = 0
            GPIO.output(DIR_PIN, GPIO.LOW)
        elif step_dir == 1:
            self.step_direction = 1
            GPIO.output(DIR_PIN, GPIO.HIGH)

    def step(self, steps=1):
        for step in range(steps):  # step n times, default is 1 step per call
            GPIO.output(STEP_PIN, GPIO.HIGH)
            time.sleep(0.001)
            GPIO.output(STEP_PIN, GPIO.LOW)
            self.angle += self.step_size  # Increment angle
            self.angle = round(self.angle, 4)

    def get_angle(self):
        return round(self.angle % 360, 4)  # mode 360 to keep between 0 and 360



