#!/usr/bin/env python
#import RPi.GPIO as gpio

import rospy
from std_msgs.msg import String
import serial


def callback(data):
    select_color = data.data
    trigger = { 'R': (5,1),'G': (6,1),'B': (7,1),'r': (5,1),'g': (6,1),'b': (7,1) }
    close   = {'C':(2,3,4,0),'c':(2,3,4,0)}
    
    ##  configure in raspberry pi  ##   

    if select_color in trigger.keys() :
        print 'The color is {} and Pin is {} '.format(select_color, trigger[select_color][0]) 
        pin   = trigger[select_color][0]
        digital_signal =trigger[select_color][1] 
        s.write("{}".format(pin).encode())  
    elif select_color in close.keys():   
        pin   = close[select_color][0:3]
        digital_signal = close[select_color][3] 
        s.write("C".encode())  
        print 'Close all.'   
    


def listener():
    
    rospy.init_node('listener_pi_01', anonymous=True)
    rospy.Subscriber("color_00", String, callback)
    rospy.spin()

if __name__ == '__main__':
    # setup the board
    s = serial.Serial("/dev/arduino_uno",9600)
    listener()
