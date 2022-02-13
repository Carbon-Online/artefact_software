# CO2online artefact software
This repository contains a software to capture your home network traffic and control a to an artefact coppled servo motor according to the amounts of captured transmitted data.

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Acknowledgements](#acknowledgements)

## Description
## project description and goal
Within the project codingXD a neo-analog artefact was designed to ... 
„Carbon online“ translates your daily digital carbon budget into a physical volume that you can monitor and balance. The budget is calculated with country-specific values for ICT energy consumption and carbon emissions to reach the 1.5 °C target. The cube is the same size as the CO2 volume of your budget and reminds you of the environmental impact beyond the screens.
* describe context of artefact and software

## software description architecture + function
The software consists of two independent processes that run simultaneously. On the one hand, there is a process that records the data traffic and stores the amount of data in bytes that is routed via the Fritzbox's internet interface. Second, a carbon budget is updated every hour. According to the emitted carbon equivalent, the state of the artefact is changed by turning a servo motor.

These two processes are represented as two classes in the processes.py module and are started in the main.py module. 

To activate the "TrafficCapturing" process, the bash script fritzdump.sh connects to a Fritzbox and reads the passing data packets at the network interfaces using tshark. These packets are piped into the terminal as stdin. Alternatively, the serverdump.sh script captures the traffic locally on the device interface. In the "TrafficCapturing" process, the IP packets are continuously read from the stdin pipe and their size is summed up in bytes. 

Every hour, the "RunArtefact" process uses this value and updates its CarbonBudget attribute accordingly. This budget is represented in the carbon_budget.py module and is reset after one day. A calculator.py module is introduced that provides calculations to convert the transmitted data into carbon equivalents. Since this is done in a separate module, more accurate and complex calculations could be introduced later. Depending on the remaining carbon budget, the state of the artifact is updated by rotating the servo motor a certain amount of steps. When only 10 percent of the daily budget is left, a warning tone sounds, and when it is used up, the tone is played twice.

![alt text](https://github.com/Carbon-Online/artefact_software/blob/main/data/artefact_software_process_architecture.png)
## Installation
The software was developed in debian [..] and those python packages are required:

"rpi.gpio" = "*"
python-vlc = "*"
python_version = "3.9"


Then the pipenv should be activated:

`pipenv install`

## Usage

## Acknowledgements

