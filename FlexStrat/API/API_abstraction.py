from abc import ABC,abstractmethod

class API_abstraction(ABC):

    def API_abstraction(self):
        self._api_name="custom api"

    def configure(self,candles,config):
        self.candles = candles
        self.config = config

    @abstractmethod
    def initialize(self):
        raise NotImplementedError


    @abstractmethod
    def create_order(self,type,open_price,open_time,size_lot,SL,TP=-1):
        raise NotImplementedError

    
    @abstractmethod
    def modify_order(self,ticket,modify_parameter,new_value):
        raise NotImplementedError

    
    @abstractmethod
    def delete_order(self,ticket):
        raise NotImplementedError


    @abstractmethod
    def run(self,next_process):
        raise NotImplementedError

    
    @abstractmethod
    def get(self,how_much=-1):
        raise NotImplementedError
