#  This is example is for the SparkFun Qwiic Twist RGB Rotary Encoder.
#  SparkFun sells these at its website: www.sparkfun.com
#  Do you like this library? Help support SparkFun. Buy a board!
#  https://www.sparkfun.com/products/15083

"""
 Qwiic Twist Simple Test - qwiictwist_simpletest.py
 Written by Gaston Williams, June 19th, 2019
 The Qwiic Twist is a I2C controlled RGB Rotary Encoder

 Simple Test:
 This program uses the Qwiic Twist CircuitPython Library to change
 that status of the Qwiic Twist Rotary Encoder.
"""

from time import sleep
import board
import busio
import sparkfun_qwiictwist

# Create bus object using our board's I2C port
i2c = busio.I2C(board.SCL, board.SDA)

# Create joystick object
twist = sparkfun_qwiictwist.Sparkfun_QwiicTwist(i2c)

# Check if connected
if twist.connected:
    print('Twist connected.')
else:
    print('Twist does not appear to be connected. Please check wiring.')
    exit()

# Print firmware version and current status
print('Firmware version ' + twist.version)

# Turn the relay on and off
print('Press Ctrl-C to exit program')

try:
    while True:
        print('Count: ' + str(twist.count))
        if twist.pressed:
            print('Pressed!')
        sleep(0.5)

except KeyboardInterrupt:
    pass
