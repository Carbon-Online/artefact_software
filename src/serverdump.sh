# Application settings
# Path to your python version in pipenv
PYTHON_PIPENV_PATH=/home/pi/.local/share/virtualenvs/artefact_software-UKji4wqU/bin/python3

PYTHON_MAIN_FILE_PATH=/home/pi/Documents/codingIxD/artefact_software/src/main.py

# get data from tshark interface capture
sudo /usr/bin/tshark -T ek | sudo $PYTHON_PIPENV_PATH $PYTHON_MAIN_FILE_PATH

