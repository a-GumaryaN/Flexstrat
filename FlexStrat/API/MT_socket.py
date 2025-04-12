from API_abstraction import API_abstraction


class MT_socket(API_abstraction):

    def initialize(self):
        pass

    def run(self,next_process):
        pass

    def create_order(self,type,open_price,open_time,size_lot,SL,TP=-1):
        pass
    
    def modify_order(self,ticket,modify_parameter,new_value):
        pass
    
    def delete_order(self,ticket):
        pass
    
    def get(self,how_much=-1):
        pass