# Lidar_Mapper_py3
scan an area with a lidar module, this project was done on a raspberry pi v3 B+. Offers multiple options for resolution.

# Hardware
Lidar Lite v3
RB-SOY-22 10V stepper motor 
SparkFun Slip Ring - 12 Wire (2A)
FS90 microservo
10V dc power supply
Pololu A4988 Stepper Driver

# Stepper 
Controlled using a A4988 stepper driver, allowing for different step sizes as well as step direction. A 10V DC power supply was used to feed the stepper 
https://www.robotshop.com/ca/en/bipolar-stepper-motor-10v-0-5a.html
https://www.robotshop.com/ca/en/8-35v-2a-single-bipolar-stepper-motor-driver-a4988-black-edition.html


# LIDAR V2
A Garmin LidarLite v3 was used, capable of measuring up to 40m, much further than needed. NOTE: if trying to use this lidar with I2C on raspian, repeated starts will cause the device to return 0. The lidarlite v3 does not support repeated start! Steps to disable repeated start can be found here: https://www.robotshop.com/community/forum/t/lidar-lite-v3-return-always-zero-with-raspberry-pi-3/27656/26/ .
smbus2 was used to interface with the lidar module.The module can be bought here:
https://www.robotshop.com/ca/en/lidar-lite-3-laser-rangefinder.html

# Servo
A FS90 microservo was used to aim the lidar module (elevation). RPi.GPIO SHOULD NOT BE USED FOR SERVO CONTROL. RPi.GPIO does not provide accurate timing for PWM, either use hardwware or another library such as pigpiod. Calculating pulse width for the servo was done by fitting a pw vs. angle curve with a 3rd order polinomial. at around 500us, the servo was at 0 degrees, and at 180 degrees with a pulse of 2500us. I measured 0, 45, 90, 135, 180 and plotted the required pulse duration to get a good fit. This fit can then be used for servo control.
 
# Libraries
pigpio, used for servo control
rpi.gpio, used for stepper
smbus2, used for lidar
Json, used for data 
open3d, used for 3d visualization (GPU)
matplotlib, used for 3d visualization, much slower for large sample sizes (No GPU)

# Results
The Setup provides multiple scan resolutions, scans can take anywhere from a minute all the way up to 30 minutes. The following scan consists of 1023802 saved in a CSV file. Visualization was done using JavaScript and ThreeJ, a Javascript library that harnesses the power of WebGL for 3D graphics. The source code for the browser visualizer can be found on my githun at:https://github.com/robotevan/PointCloudVisualizer. 
![Image of Point Cloud](https://github.com/robotevan/Lidar_Mapper_py3/blob/master/RoomScan.png)
