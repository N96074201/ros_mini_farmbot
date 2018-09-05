#!/bin/bash
set -e

if [[ `id -u` -eq 0 ]] ; then
    echo "Do not run this with sudo (do not run random things with sudo!)." ;
    exit 1 ;
fi

set -x


sudo apt install -y \
	 ros-kinetic-uvc-camera \
         ros-kinetic-image-* \
         ros-kinetic-rqt-image-view \
         ros-kinetic-camera-calibration \
         python-imaging-tk \
        	
# These don't have an APT package

pip install pmw
	




# None of this should be needed. Next time you think you need it, let me know and we figure it out. -AC
# sudo pip install --upgrade pip setuptools wheel
