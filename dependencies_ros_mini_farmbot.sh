#!/bin/bash


if [[ `id -u` -eq 0 ]] ; then
    echo "Do not run this with sudo (do not run random things with sudo!)." ;
    exit 1 ;
fi

# Use APT install
sudo apt-get install -y \
	 ros-kinetic-uvc-camera \
         ros-kinetic-image-* \
         ros-kinetic-rqt-image-view \
         ros-kinetic-camera-calibration \
         ros-kinetic-find-object-2d \
         libopencv-dev \
         libqt4-dev \
         python-imaging-tk \
         python-pip \
         python-configobj	

# These don't have an APT package

# about mini_farmbot gui_main.py
pip install pmw
	




# None of this should be needed. Next time you think you need it, let me know and we figure it out. -AC
# sudo pip install --upgrade pip setuptools wheel
