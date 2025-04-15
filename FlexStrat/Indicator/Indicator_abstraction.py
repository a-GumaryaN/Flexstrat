from abc import ABC, abstractmethod
from ..Module import Abstract_module

class Indicator_abstraction(Abstract_module):

    def __init__(self):
        # last index that indicator calculated
        self.last_calculated_index = 0
        self.indicator_id="custom indicator instance"
        self.depends_to="data"

    # this method will run in initialization phase
    @abstractmethod
    def initialize(self)->str:
        pass

    # this method will run in execution phase
    @abstractmethod
    def run(self)->None:
        raise NotImplementedError