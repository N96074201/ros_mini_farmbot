#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def callback(data):
    select_color = data.data
    trigger = { 'R': (9,1),'G': (10,1),'B': (11,1),'r': (9,1),'g': (10,1),'b': (11,1) }
    close   = {'C':(9,10,11,0),'c':(9,10,11,0)}
    if select_color in trigger.keys() :
        print 'The color is {} and Pin is {} '.format(select_color, trigger[select_color][0]) 
        pin   = trigger[select_color][0]
        digital_signal =trigger[select_color][1]   
    elif select_color in close.keys():   
        pin   = close[select_color][0:3]
        digital_signal = close[select_color][3]   
        print 'Close all.'   
    

def listener():
    
    rospy.init_node('listener_computer_00', anonymous=True)
    rospy.Subscriber("color_00", String, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
