#!/bin/bash


if [[ `id -u` -eq 0 ]] ; then
    echo "Do not run this with sudo (do not run random things with sudo!)." ;
    exit 1 ;
fi


sudo mkdir ~/.ros/camera_info 
sudo chmod 0777 ~/.ros/camera_info 
sudo cp ~/ros_mini_farmbot/camera_calibration/camera.yaml ~/.ros/camera_info/camera.yaml




# None of this should be needed. Next time you think you need it, let me know and we figure it out. -AC
# sudo pip install --upgrade pip setuptools wheel
