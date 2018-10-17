# ros_mini_farmbot

This repository contains the gui software that runs on the Minifarmbot.

# reference

FBTUG-FarmBot Taiwan User Group   :  https://paper.dropbox.com/doc/FBTUG-FarmBot-Taiwan-User-Group-h0jWbePzd7PkmIN0ZxkYx

# src/first_pkg

This package use Arduino uno and pyserial to introduce and learn GPIO with ROS.

Because Arduino Mega for Minifarmbot use the G-code driver, we don't use rosserial on Arduino.

# src/minifarm

This package contains the gui software of Minifarmbot

# Operate

* 1. Start roscore at laptop 
  
  ` roscore `

* 2. run " uvc_camera_node " at laptop
  
  ` rosrun uvc_camera uvc_camera_node `
  
* 3. run " find_object_2d " at laptop . Note the topic with image. 

  ` rosrun find_object_2d find_object_2d image:=/image_raw`
 
* 4. add items in the windoes of find_object_2d
 
* 5. run " listen_topic_objects.py " at laptop

  ` rosrun first_pkg listen_topic_objects.py`
  
* 6. run " listen_topic_objects.py " at raspberryPi . Note arduino must be connected with raspberryPi and Open permission

  ` rosrun first_pkg listen_topic_objects.py`
