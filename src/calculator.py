import math


class Calculator:
    """
    A Calculator class doing the required calculation to convert capture data traffic
    into used carbon and steps the artefact motor has to turn.
    """

    def __init__(self, traffic_amount, carbon_per_traffic, steps_per_carbon):
        #: Data traffic amount capture in GB gets converted from
        # bytes to gigabytes
        self.traffic_amount = traffic_amount * 0.000000001
        #: Carbon which is used per GB
        self.carbon_per_traffic = carbon_per_traffic
        #: Steps to be turned according to a gram carbon
        self.steps_per_carbon = steps_per_carbon
        #: Carbon used the last hour
        self.used_carbon = self.traffic_data_to_carbon()
        #: Current steps the motor has to be turned
        self.steps_to_turn = self.carbon_to_steps()

    def traffic_data_to_carbon(self):
        """
        Calculates the data traffic produced carbon amount.

        :return: a float of CO2 in gram
        """
        return self.traffic_amount * self.carbon_per_traffic

    def carbon_to_steps(self):
        """
        Calculates the steps to turn for a motor according the
        produced carbon.

        :return: int in steps
        """
        return math.ceil(self.steps_per_carbon * self.used_carbon)
