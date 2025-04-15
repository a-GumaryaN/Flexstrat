from ..Module import Abstract_module
from abc import abstractmethod
from ..Data import Shared_data

class Visualizer_abstraction(Abstract_module):

    def Visualizer_abstraction(self):
        self._visualizer_name = "custom visualizer"

    def create_object(self,new_object):
        self.shared_data.data["objects"].append(new_object)

    @abstractmethod
    def initialize(self)->None:
        pass
    
    @abstractmethod
    def run(self)->None:
        pass