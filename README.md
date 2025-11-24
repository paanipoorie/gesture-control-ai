# AI Hand Gesture Control System

A simple computer vision–based gesture controller that launches applications on Linux using hand gestures tracked via webcam.

## Features
- Fist → Open Calculator
- One finger → Open Calendar
- Three fingers → Open Brave Browser
- Four fingers → Open VS Code
- Real-time gesture tracking using CVZone HandTrackingModule
- Cooldown system to prevent repeated triggers

## Tech Stack
- Python
- OpenCV
- CVZone

## To Run
pip install -r requirements.txt
source ~/gesture-env/bin/activate
python ~/gesture_control.py
