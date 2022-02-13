# CO2online artefact software
This repository contains a software to capture your home network traffic and control a to an artefact coppled servo motor according to the amounts of captured data.

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Acknowledgements](#acknowledgements)

## Description
Within the project codingXD a neo-analog artefact was designed to ...
In order to track your internet usage via data traffic the software enables a raspberry pi to log into the fritzbox and pipe into the software the packages. 
The software architecture is composed by two independet processes running concurrently. First an ongoing process capturing the data traffic and saving the amount of data in bytes passed through the fritzbox wifi interface. Second an hourly update of a carbon budget

## Installation
The software was developed in debian [..] and those python packages are required:

"rpi.gpio" = "*"
python-vlc = "*"
python_version = "3.9"


Then the pipenv should be activated:

`pipenv install`

## Usage

## Acknowledgements

