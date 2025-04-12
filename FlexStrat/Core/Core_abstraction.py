from abc import ABC,abstractmethod

class Core_abstraction(ABC):

    def configure(self,config,shared_data):
        self.config = config
        self.shared_data= shared_data

    @abstractmethod
    def initialize(self,config,shared_data):
        pass

    @abstractmethod
    def run(self,config,shared_data):
        pass