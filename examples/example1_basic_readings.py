#  This is example is for the SparkFun Qwiic Single Twist.
#  SparkFun sells these at its website: www.sparkfun.com
#  Do you like this library? Help support SparkFun. Buy a board!
#  https://www.sparkfun.com/products/15083

"""
 Qwiic Twist Example 1 - example1_basic_readings.py
 Written by Gaston Williams, June 19th, 2019
 Based on Arduino code written by
 Nathan Seidle @ Sparkfun, December 3rd, 2018
 The Qwiic Twist is an I2C controlled RGB Rotary Encoder produced by sparkfun

 Example 1 - Basic Readings:
 This program uses the Qwiic Twist CircuitPython Library to
 control the Qwiic Twist RGB Rotrary Encoder over I2C and print
 the number of steps the encoder has been twisted.
"""

from time import sleep
import board
import busio
import sparkfun_qwiictwist

# Create bus object using our board's I2C port
i2c = busio.I2C(board.SCL, board.SDA)

# Create twist object
twist = sparkfun_qwiictwist.Sparkfun_QwiicTwist(i2c)

print('Qwicc Twist Example 1 Basic Readings')

# Check if connected
if twist.connected:
    print('Twist connected.')
else:
    print('Twist does not appear to be connected. Please check wiring.')
    exit()

print('Type Ctrl-C to exit program.')

try:
    while True:
        print('Count: ' + str(twist.count))
        if twist.pressed:
            print('Pressed!')
        sleep(0.5)

except KeyboardInterrupt:
    pass
