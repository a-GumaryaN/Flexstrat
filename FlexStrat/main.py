from .API import API_repository
from .Indicator import Indicator_repository
from .Core import Core_repository
from .Trade_manager import Trade_manager_repository
from .Visualizer import Visualizer_repository
import json
from .config import ModuleConfig
import os
import importlib.util
from termcolor import colored

def load_section(config,file_extension):
    for directory in config["src"]:
        current_directory = os.getcwd()
        api_directory = os.path.join(current_directory,directory)
        if not os.path.isdir(api_directory):
            error = f"Failed to open api directory {api_directory}"
            print(colored(error,"red"))
            exit(1)
        python_files = [
            f for f in os.listdir(api_directory) 
            if f.endswith(file_extension)
        ]
        for file in python_files:
            file_path = os.path.join(api_directory, file)
            module_name = file[:-3]
            
            try:
                spec = importlib.util.spec_from_file_location(module_name, file_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
            except Exception as e:
                error = f"Failed to load api module {file}"
                print(colored(error,"red"))
                print(colored(e,"red"))
                exit(0)

def get_extension(section):
    if section == "api":
        return '_api.py'
    elif section == "indicator":
        return "_ind.py"
    elif section == "script":
        return "_scr.py"
    elif section == "core":
        return "_core.py"
    elif section == "visualizer":
        return "_vis.py"
    elif section == "trade_manager":
        return "_trm.py"
    else :
        return "_ext"

def load_modules(config):
    for section in config:
        extension = get_extension(section)
        load_section(config[section],extension)

def load_config(config_path):
    with open(config_path) as file:
        return json.load(file)

def validate_config(config):
    pass

def load_repositories(config_path):
    config = load_config(config_path)
    validate_config(config)
    load_modules(config)

class Basement:

    def __init__(self,config_path="config.json"):
    
        load_repositories(config_path)

        self.repositories = dict({})

        self.repositories["api"] = API_repository()
        self.repositories["indicator"] = Indicator_repository()
        self.repositories["visualizer"] = Visualizer_repository()
        self.repositories["core"] = Core_repository()
        self.repositories["trade_manager"] = Trade_manager_repository()

    def show_repositories(self):
        for repository in self.repositories:
            print(colored(f"AVAILABLE {repository.upper()} :","green"))
            for item in self.repositories[repository].repository :
                print(colored(f"    ● {item}","green"))
            print()