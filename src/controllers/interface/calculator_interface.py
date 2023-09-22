from abc import ABC, abstractmethod
from src.main.http_types.http_request import HttpRequest


class ICalculator(ABC):
    @abstractmethod
    def execute(self, req: HttpRequest): pass
