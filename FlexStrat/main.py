import pandas as pd
from .IOC_manager import IOC_manager
from .constant import *
from termcolor import colored
from threading import Thread
from .API import *
from .Visualizer import *
from .Indicator import *

trades = pd.DataFrame(columns=["open_time","open_price","status","type","close_time","SL","TP","size_lot"])

class Basement:

    api_interface = None
    visualizer = None
    indicators = []
    core = None


    api_thread=None
    visualizer_thread=None
    event_handler_thread=None

    indicators_tree = []

    def __init__(self):
        # initialize ioc manager
        self.ioc_manager = IOC_manager()
        self.ioc_manager.register(API,"csv_api",CSV)
        self.ioc_manager.register(VISUALIZER,"mpl",MPL_visualizer)
        self.ioc_manager.register(VISUALIZER,"CDD",CDD)

    def run_indicators(self):
        pass

    def run_core(self):
        self.core.run()

    def initialize_indicators_tree(self):
        pass

    def event_handler(self):
        pass

    def add(self,module_section,module_name,module):
        self.ioc_manager.register(module_section,module_name,module)

    def initialize(self,config):
        # set system configuration
        self.config = config
        # initialize shared data
        self.shared_data={
            "candles":pd.DataFrame(columns=["open","close","high","low","volume"]),
            "indicators":[],
            "objects":[]
        }
        #   initialize dependencies
        #       initialize api interface
        if API not in self.config:
            raise Exception("NO CONFIGURATION FOUND FOR API")
        api_config = self.config[API]
        self.api_interface = self.ioc_manager.contain(API,api_config["name"])
        self.api_interface.configure(self.shared_data,api_config)

        #       initialize visualizer
        if VISUALIZER not in self.config: 
            print(colored('WARNING : NO CONFIGURATION FOUND FOR VISUALIZER, SYSTEM WILL WORK WITHOUT VISUALIZING', 'red'))
        else :
            visualizer_config = self.config[VISUALIZER]
            self.visualizer = self.ioc_manager.contain(VISUALIZER,visualizer_config["name"])
            self.visualizer.configure(self.shared_data,visualizer_config)

        #      initialize indicators
        if INDICATORS in self.config:
            for indicator_config in self.config[INDICATORS]:
                indicator = self.ioc_manager.contain(INDICATORS,indicator_config["type"])
                indicator.configure(self.shared_data,indicator_config)
                self.indicators.append(indicator)

        if CORE not in self.config:
            print(colored('WARNING : NO CONFIGURATION FOUND FOR CORE, SYSTEM WILL WORK IN TEST MODE', 'red'))
        else :
            core_config = self.config[CORE]
            self.core = self.ioc_manager.contain(CORE,core_config["name"])
            self.core.configure(self.shared_data,core_config)
        
        return "system initialized successfully"

    #   this method will start system
    def run(self):
        # creating threads
        self.api_thread = Thread(self.api_interface.run,)

        if self.visualizer :
            self.visualizer_thread = Thread(self.api_interface.run)

        self.event_handler_thread = Thread(self.event_handler)

        
             
