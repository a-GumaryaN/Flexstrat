from .API_abstraction import API_abstraction
import pandas as pd

class  CSV(API_abstraction):
    __counter=0
    __data=None
    __data_len =0

    def create_order(self,type,open_price,open_time,size_lot,SL,TP=-1):
        pass
    
    def modify_order(self,ticket,modify_parameter,new_value):
        pass
    
    def delete_order(self,ticket):
        pass

    def initialize(self):
        self.__data = pd.read_csv(self.config["file_path"])
        self.__data_len = len(self.__data)
        self.__data.reset_index(drop=False, inplace=True)
        self.__data["datetime"] = self.__data["date"] + " " + self.__data["time"]
        self.__data["datetime"] = pd.to_datetime(self.__data["datetime"])

    def get(self):
        how_much = self.config["initial_data"]
        self.__counter = how_much
        if how_much == -1:
            return self.__data
        return self.__data.iloc[:how_much];

    def run(self,next_process):
        self.__counter+=1
        if self.__counter <= self.__data_len:
            self.candles = self.__data[:self.__counter]
            next_process()

    def API_abstraction(self):
        self._api_name="custom api"

    def configure(self,candles,config):
        self.candles = candles
        self.config = config