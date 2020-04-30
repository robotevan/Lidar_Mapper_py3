from Lidar import Lidar
#from plotter import Plot
from Stepper import Stepper
from Servo import Servo
from mpl_toolkits.mplot3d import axes3d, Axes3D
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math
import json
import time
import RPi.GPIO as GPIO


stepper = Stepper()
servo = Servo()
lidar = Lidar()
servo.set_angle(0)
time.sleep(1)

def _sphere_to_cart_(r, theta, phi):
    theta = math.radians(theta)
    phi = math.radians(phi)
    x = r*(math.sin(phi))*(math.cos(theta))  # get x
    y = r*(math.sin(phi))*(math.sin(theta))  # get y
    z = r*(math.cos(phi))  # get z
    return [x, y, z]  # return coord for point in cart


data = {}

point = 0
for ang in range(100):
    for step in range(202):
        r = lidar.read_distance()
        phi = servo.read_angle()
        theta = stepper.get_angle()
        #time.sleep(0.2)
        coord = _sphere_to_cart_(r, theta, phi)
        print("pol:" + str([r, phi, theta]) + "cart: " + str(coord))
        if r< 600:
            data[point] = [coord[0], coord[1], coord[2]]
        point+=1
        stepper.step()
        servo.set_angle(ang)
with open('coords.json', mode='w') as coords_json:
    json.dump(data, coords_json, indent=2)
#plot = Plot()
GPIO.cleanup()