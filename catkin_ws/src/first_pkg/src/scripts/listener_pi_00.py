#!/usr/bin/env python
#import RPi.GPIO as gpio

import rospy
from std_msgs.msg import String
import serial
from pyfirmata import Arduino, util 


def callback(data):
    select_color = data.data
    trigger = { 'R': (2,1),'G': (3,1),'B': (4,1),'r': (2,1),'g': (3,1),'b': (4,1) }
    close   = {'C':(2,3,4,0),'c':(2,3,4,0)}
    if select_color in trigger.keys() :
        print 'The color is {} and Pin is {} '.format(select_color, trigger[select_color][0]) 
        pin   = trigger[select_color][0]
        digital_signal =trigger[select_color][1]   
    elif select_color in close.keys():   
        pin   = close[select_color][0:3]
        digital_signal = close[select_color][3]   
        print 'Close all.'   
    
    ##  configure in raspberry pi  ##   
    # setup the board
    board = Arduino('/dev/arduino_uno')
    board.digital[pin].write(digital_signal)

def listener():
    
    rospy.init_node('listener_pi_00', anonymous=True)
    rospy.Subscriber("color_00", String, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
