# 3D-Bionics Hand Control

Software for controlling a 3D printed Hand with python and an Arduino.

## Overview

### Communication-Framework

The communication framework provides an interface for communicating between another device and the arduino over serial. It uses [pyserialtransfer](https://github.com/PowerBroker2/pySerialTransfer) as a back-end for transfers over serial.

### Terminal User Interface

The HandControll Package provides a Terminal User Interface for controlling the hand via a series of sliders for each finger and pre-programmed commands for certain gestures

## Dependencies

To use this programm you need:
-   npyscreen
-   [pyserialtransfer](https://github.com/PowerBroker2/pySerialTransfer)

You need to install these via pip first
