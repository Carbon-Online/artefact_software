import math

# Total (!) path to played audio file
PATH_TO_AUDIO = "/home/pi/Documents/codingIxD/cloud-to-cloud/data/thriller.mp3"

# Pin of raspberry pi for the motor
GPIO_PIN_MOTOR =  [18, 17, 27, 22]

# Daily carbon budget per person
# in g per CO2
DAILY_CARBON_BUDGET = 102.5 / 60

# ENERGY_PER_INTERNET_TRAFFIC = 0.01
# CARBON_EMISSION_PER_ENERGY = 0.401
# CO2 in g per GB
CARBON_PER_GB = 4.01

# Number of steps of the artefact motor per carbon use
DEGREE_PER_CARBON = math.floor(DAILY_CARBON_BUDGET / 3800)
