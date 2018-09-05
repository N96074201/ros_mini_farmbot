#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32MultiArray , String

def callback(data):
    detect_MultiArray = data.data
    detect_object = detect_MultiArray[0]
    

def listener():
    
    rospy.init_node('listener_topic_objects', anonymous=True)
    rospy.Subscriber("objects",Float32MultiArray , callback)   
    rospy.spin()

if __name__ == '__main__':
    listener()
