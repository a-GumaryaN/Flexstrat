from abc import ABC,abstractmethod

class Visualizer_abstraction(ABC):

    def Visualizer_abstraction(self):
        self._visualizer_name = "custom visualizer"

    def config(self,config,shared_data):
        self.config = config
        self.shared_data = shared_data

    @abstractmethod
    def initialize(self,shared_data):
        pass
    
    @abstractmethod
    def run(self):
        pass