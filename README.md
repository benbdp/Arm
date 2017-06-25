We are working on building a 3 jointed arm that will be used to pick ripe tomatoes from a plant.

Sensors connected to an Arduino collect a veriety of data to be used to moitor the enviroment of the plants. 

The arm slides along the plants on a custom rail controlled by a stepper motor and Arduino.

The two Arduinos are connected to a Raspberry Pi. The Raspberry Pi is used to control the arm and the position of the carriage on the rail.

A camera on the carriage is used to identify the position of the plants. The camera interfaces with an Nvidia Jetson TK1.

The Raspberry Pi interfaces with the servos using a USB2AX.

Ax12 Library: https://pypi.python.org/pypi/pyax12

Will Doyle and Ben Plamondon
