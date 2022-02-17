# CO<sub>2</sub>NLINE artefact software
This repository contains a software to capture your home network traffic and control a to an artefact coppled servo motor according to the amounts of captured transmitted data.

## Contents
* [Description](#description)
  + [Base project](#base-project)
  + [Functionality and architecture](#functionality-and-architecture)
  + [Implementation](#implementation)
  + [Technical setup](#technical-setup)
* [Installation](#installation)
* [Usage](#usage)
* [Acknowledgements](#acknowledgements)

## Description
### Base project
This application belongs to the CO2NLINE project which was created and implemented as part of the coding IxD lecture of the FU Berlin and the KH Weissensee. The topic was Digital Souveranity. CO2NLINE is an artefact that visualizes one's digital carbon footprint.

### Functionality and architecture
The software consists of two independent processes that run simultaneously. On the one hand, there is a process that records the data traffic and stores the amount of data in bytes that is routed via the Fritzbox's internet interface. Second, a carbon budget is updated every hour. According to the emitted carbon equivalent, the state of the artefact is changed by turning a servo motor.

These two processes are represented as two classes in the processes.py module and are started in the main.py module. 

To activate the "TrafficCapturing" process, the bash script fritzdump.sh connects to a Fritzbox and reads the passing data packets at the network interfaces using tshark. These packets are piped into the terminal as stdin. Alternatively, the serverdump.sh script captures the traffic locally on the device interface. In the "TrafficCapturing" process, the IP packets are continuously read from the stdin pipe and their size is summed up in bytes. 

Every hour, the "RunArtefact" process uses this value and updates its CarbonBudget attribute accordingly. This budget is represented in the carbon_budget.py module and is reset after one day. A calculator.py module is introduced that provides calculations to convert the transmitted data into carbon equivalents. Since this is done in a separate module, more accurate and complex calculations could be introduced later. Depending on the remaining carbon budget, the state of the artifact is updated by rotating the servo motor a certain amount of steps. When only 10 percent of the daily budget is left, a warning tone sounds, and when it is used up, the tone is played twice.

![alt text](https://github.com/Carbon-Online/artefact_software/blob/main/data/artefact_software_process_architecture.png)

A settings.py file provides the made value settings for the daily budget, the carbon data equivalents and number of total number of turns of the motor for one daily circle. 

### Implementation
The software is developed in debian on a Raspberry pi 3 Model B as it is capable to control a servo motor, display sounds and capture the data traffic. The following system version is used:
```
Distributor ID: Raspbian
Description: Raspbian GNU/Linux 9.13 (stretch)
Release: 9.13
Codename: stretch
```
The software is implemented using Shell and Python. The shell scripts are used to capture the data traffic and build a pipe. Therefore tshark (Version: `TShark (Wireshark) 2.6.20 (Git v2.6.20 packaged as 2.6.20-0+deb9u2)`) is used because it can read binary pcap files written by the Fritzbox. Python has a wide range of libraries and is easy to handle. This is used to combine the functionality of reading the pipe and controlling the artefact.
Therefore following python package versions were used:
```
"rpi.gpio" = "*"
python-vlc = "*"
rpimotorlib = "*"
```
### Technical setup

A [NEMA 11-size hybrid bipolar stepping motor](https://www.pololu.com/product/1205/specs) is used which has 200 steps per revolution, and can operate at at 60 RPM. 

The motor is controlled and connected to the raspberry pi via a [L298N H-bridge](http://www.st.com/resource/en/datasheet/l298.pdf).

The hardware is connected like shown here ([Image source](https://i.stack.imgur.com/JyKhm.jpg)):
![alt text](https://github.com/Carbon-Online/artefact_software/blob/main/data/technical_setup.png)

In this setup the raspberry Pi GPIO Pins = [18, 17, 27, 22] are choosen.

Further details can be found in this [tutorial](https://github.com/gavinlyonsrepo/RpiMotorLib/blob/master/Documentation/Nema11L298N.md).

## Installation
**!! Make sure you have tshark, Python 3.9 and pipenv installed. !!**

1. Clone the repository from git:
```
git clone https://github.com/Carbon-Online/artefact_software.git
```
2. Navigate to the project and activate the pipenv once:
``` 
cd artefact_software
pipenv install
```
3. Adapt the settings (path to media file, GPIO pins used) in the src/settings.py file using your favorite texteditor.
4. Adapt the settings in the src/fritzdump.sh and the scr/serverdump.sh file (Fritzbox login data, path to pipenv and src/main.py file) using your favorite texteditor.
5. Connect the GPIO pins of the raspberry pi with the treiber and the motor.
6. Connect the raspberry pi to the desired network and a sound device via eg.`raspi-config`.

## Usage
1. Start to sniff the data traffic on your fritzbox: 
```
bash src/fritzboxdump.sh
```
2. Or on your local device interface:
```
bash src/serverdump.sh
```
Play around with your budget and change therefore the settings in the settings.py file.

## Acknowledgements
Programming: Julia Mellert
