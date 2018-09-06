#!/usr/bin/env python

# python and ROS
import rospy    
from std_msgs.msg import Float32MultiArray , String

# python and serial   
import serial    

# python and operating system
import time , os

# python read .ini
import ConfigParser

# conect Arduino
arduino_uno = serial.Serial("/dev/arduino_uno" , 9600)

# read ~/.ros/find_object_2d.ini
config = ConfigParser.ConfigParser() 
config.read(os.path.expanduser('~/.ros/find_object_2d.ini'))
start_objID = config.getint('%General','nextObjID')
red   = start_objID
green = red + 1
blue  = green + 1

def callback(data):
    detect_MultiArray = data.data
    if detect_MultiArray :
        detect_object = detect_MultiArray[0]
        if detect_object == red :
            arduino_uno.write('2'.encode())
            print 'red'
        elif detect_object == green :
            arduino_uno.write('3'.encode())
            print 'green'
        elif detect_object == blue :
            arduino_uno.write('4'.encode())
            print 'blue'
    else :
        arduino_uno.write('F'.encode())
        print 'No object !'

def listener():
    
    rospy.init_node('listener_topic_objects', anonymous=True)
    rospy.Subscriber("objects",Float32MultiArray , callback)   
    rospy.spin()

if __name__ == '__main__':
    listener()
