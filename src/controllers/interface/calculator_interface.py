from abc import ABC, abstractmethod


class ICalculator(ABC):
    @abstractmethod
    def calculate(self, values): pass
