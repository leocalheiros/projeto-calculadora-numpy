import numpy as np


class CalculationManager:
    def __init__(self) -> None:
        self.__np = np

    def average(self, values):
        return self.__np.average(values)

    def variance(self, values):
        return self.__np.var(values)

    def std_deviation(self, values):
        return self.__np.std(values)
