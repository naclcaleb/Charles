#!/bin/bash
cd ~
#Download the project files
wget https://raw.githubusercontent.com/naclcaleb/Charles/experimental/devices/pi_zero/main.py
cd Charles_core
wget https://raw.githubusercontent.com/naclcaleb/Charles/experimental/devices/pi_zero/Charles_core/Charles.py
wget https://raw.githubusercontent.com/naclcaleb/Charles/experimental/devices/pi_zero/Charles_core/Indicator.py
wget https://raw.githubusercontent.com/naclcaleb/Charles/experimental/devices/pi_zero/Charles_core/SpeechRecognition.py
wget https://raw.githubusercontent.com/naclcaleb/Charles/experimental/devices/pi_zero/Charles_core/Voice.py
wget https://raw.githubusercontent.com/naclcaleb/Charles/experimental/devices/pi_zero/Charles_core/WakeWord.py
wget https://github.com/naclcaleb/Charles/blob/experimental/devices/pi_zero/Charles_core/__init__.py
