from abc import ABC,abstractmethod
from ..Data import Shared_data

class Abstract_module(ABC):

    # this method is run in Basement class in initialization phase
    def configure(self,config):
        self.config = config
        self.shared_data = Shared_data()

    @abstractmethod
    def initialize(self):
        raise NotImplementedError
    
    @abstractmethod
    def run(self):
        raise NotImplementedError