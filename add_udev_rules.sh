#!/bin/bash


if [[ `id -u` -eq 0 ]] ; then
    echo "Do not run this with sudo (do not run random things with sudo!)." ;
    exit 1 ;
fi

# copy the rules to /etc/udev/rules.d

sudo cp ~/ros_mini_farmbot/catkin_ws/src/first_pkg/uno_driver/uno.rules /etc/udev/rules.d/uno.rules

sudo udevadm control --reload-rules
sudo udevadm trigger


	




# None of this should be needed. Next time you think you need it, let me know and we figure it out. -AC
# sudo pip install --upgrade pip setuptools wheel
