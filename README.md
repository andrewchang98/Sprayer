# Sprayer

Sprayer is the repository for the code that runs on Unifarmers' Dual Sensor Sprayer Module.

The Dual Sensor Sprayer Module is a circuit board which seats two Raspberry Pi 3+ Compute Modules (CM3+).

The latest circuit board revision currently used connects two Raspberry Pi V2 Camera Modules
independently to their respective CM3+. A single hardware output pin is used for each CM3+, and both
outputs of the CM3+ are combined using a hardware OR logic gate to (in principle) double the effectiveness
of the detection rate and introduce redundancy.

https://picamera.readthedocs.io/en/release-1.13/ is an excellent resource for understanding the Pi Camera.

Firmware.py is the simple script which captures images and scans a single center line to check for the presence of "green" pixels.

Green is currently measured in the code using three variables based on the RGB value of a pixel.
