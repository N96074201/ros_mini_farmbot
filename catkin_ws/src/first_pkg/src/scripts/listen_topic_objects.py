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
try:
    arduino_uno = serial.Serial("/dev/arduino_uno" , 9600)
    connect = 1
except serial.SerialException:
    connect = 0
    print '\nno connection ! \n'

# judge ~/.ros/find_object_2d.ini exists?
file_path = os.path.expanduser('~/.ros/find_object_2d.ini')
if os.path.isfile( file_path ):
    # read ~/.ros/find_object_2d.ini and set ros parameter
    config = ConfigParser.ConfigParser() 
    config.read(file_path)
    start_objID = config.getint('%General','nextObjID')
    rospy.set_param('~start_objID',start_objID)
    print 'find_object_2d.ini exists ! Use it!\n'
else:
    start_objID = rospy.get_param('~start_objID')
    print 'find_object_2d.ini do not exist ! get ros parameter from /start_objID \n'

red   = start_objID
green = red + 1
blue  = green + 1

def callback(data):
    detect_MultiArray = data.data
    if detect_MultiArray :
        detect_object = detect_MultiArray[0]
        if detect_object == red :
            if connect == 1:
                arduino_uno.write('2'.encode())
            print 'red'
        elif detect_object == green :
            if connect == 1:
                arduino_uno.write('3'.encode())
            print 'green'
        elif detect_object == blue :
            if connect == 1:
                arduino_uno.write('4'.encode())
            print 'blue'
    else :
        if connect == 1 :
            arduino_uno.write('F'.encode())
        print 'No object !'

def listener():
    
    rospy.init_node('listener_topic_objects', anonymous=True)
    rospy.Subscriber("objects",Float32MultiArray , callback)   
    rospy.spin()

if __name__ == '__main__':
    listener()
