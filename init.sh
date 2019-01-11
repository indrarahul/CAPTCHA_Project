#!/bin/bash
sudo apt-get install chromium-browser
wget https://chromedriver.storage.googleapis.com/2.45/chromedriver_linux64.zip
cd /Downloads
unzip https://chromedriver.storage.googleapis.com/2.45/chromedriver_linux64.zip
chmod a+x chromedriver
mv chmod a+x chromedriver /usr/bin
sudo apt install python3-pip
pip3 install selenium pyautogui Xlib opencv-python
sudo apt-get install scrot
sudo add-apt-repository ppa:maarten-baert/simplescreenrecorder
sudo apt update
sudo apt install simplescreenrecorder simplescreenrecorder-lib
