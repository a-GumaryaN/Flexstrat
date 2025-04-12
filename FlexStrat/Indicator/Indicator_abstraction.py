from abc import ABC, abstractmethod

class Indicator_abstraction(ABC):

    def __init__(self):
        # last index that indicator calculated
        self.last_calculated_index = 0
        self.indicator_name="custom indicator"
        self.depends_to=""

    def configure(self,shared_data,config):
        self.config = config
        self.shared_data= shared_data
        self.name = self.config["name"]

    # this method will run in initialization phase
    @abstractmethod
    def initialize(self):
        raise NotImplementedError

    # this method will run in execution phase
    @abstractmethod
    def run(self):
        raise NotImplementedError