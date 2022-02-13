# CO2online artefact software
This repository contains a software to capture your home network traffic and control a to an artefact coppled servo motor according to the amounts of captured data.

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Acknowledgements](#acknowledgements)

## Description
## project description and goal
Within the project codingXD a neo-analog artefact was designed to ...

## software description architecture + function
In order to track your internet usage via data traffic the software enables a raspberry pi to log into the fritzbox and pipe into the software the packages. 
The software architecture is composed by two independet processes running concurrently. First an ongoing process capturing the data traffic and saving the amount of data in bytes passed through the fritzbox wifi interface. Second an hourly update of a carbon budget is calculated and according to the emitted carbon equivalent the state of the artefact by rotating a servo motor is changed.

Those two processes are reprrsented as two classes in the processes.py module and are started within  the main.py module. The "CaptureTraffic"
 process reads from a stdin pipecontinuesly ip packages captured in json format and sums up their amount in bytes. The "RunArtefact" takes this value and updates its attribute a CarbonBudget which is represented in the carbon_budgte.py module. therefore a calculator.py module was introduced which provides calculations to translate the data traffic used into carbon equivalent. as this is done in a seperate module later more accurate and complex calculations can be implemented . depending on the left over carbon budget the artefact state is updated via turning the servo motor inta certain amount of dgrees. if just 10 percent of daily budget is left a sound is played as a warning and if it is used up the sound is played twice.
## Installation
The software was developed in debian [..] and those python packages are required:

"rpi.gpio" = "*"
python-vlc = "*"
python_version = "3.9"


Then the pipenv should be activated:

`pipenv install`

## Usage

## Acknowledgements

