import math

# Total (!) path to played audio file
PATH_TO_AUDIO = "/home/pi/Documents/codingIxD/artefact_software/data/thriller.mp3"

# Pins of raspberry pi for the motor
GPIO_PINS_MOTOR = [18, 17, 27, 22]

# Daily carbon budget per person
# in g per CO2
DAILY_CARBON_BUDGET = 102.5 / 60

# ENERGY_PER_INTERNET_TRAFFIC = 0.01
# CARBON_EMISSION_PER_ENERGY = 0.401
# CO2 in g per GB
CARBON_PER_GB = 4.01

# Number of steps of the artefact motor per carbon use
STEPS_PER_CARBON = DAILY_CARBON_BUDGET / 3800
