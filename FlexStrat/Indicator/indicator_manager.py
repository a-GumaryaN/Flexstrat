from .Indicator_abstraction import Indicator_abstraction
import networkx as nx
from ..constant import INDICATORS
from ..Data import Shared_data

import matplotlib.pyplot as plt

class Indicator_manager:
    def __init__(self):
        self.indicators = []
        self.repository = {}
        self.shared_data = Shared_data()

    def add_indicator(self,indicator_name:str,indicator_class:Indicator_abstraction):
        if indicator_name in  self.repository:
            duplication_name_error = "indicator with name "+indicator_name+" is already exist in indicators"
            raise Exception(duplication_name_error)
        self.repository[indicator_name] = indicator_class

    def create_indicator_tree(self):
        self.indicator_graph = nx.Graph()
        edges = []
        for indicator in self.indicators:
            if type(indicator.depends_to) == str and indicator.depends_to != "":
                edges.append((indicator.config["name"],indicator.depends_to))
            elif type(indicator.depends_to) == list :
                for dependency in indicator.depends_to :
                    edges.append((indicator.config["name"],dependency))
        self.indicator_graph.add_edges_from(edges)
    
    def show_dependency_graph(self):
        nx.draw(self.indicator_graph, with_labels=True, node_color='lightblue', edge_color='gray')
        plt.show()

    def construct_indicators(self,indicators_config):
        # create indicators instantiated
        for indicator_config in indicators_config:
            # get indicator class from indicator repository with indicator name
            Indicator_class = self.repository[indicator_config["from"]]
            # create an instantiate
            indicator = Indicator_class()
            # configure indicator
            indicator.configure(indicator_config)
            # add a space in shared data indicators
            # this space will contain indicator data during execution
            # other process only can read that
            indicator_name = indicator_config["name"]
            self.shared_data.data["indicators"][indicator_name] = None
            # add indicator to indicators array
            self.indicators.append(indicator)
        # find indicators hierarchy
        self.find_hierarchy()

    def find_hierarchy(self):
        # construct indicator tree
        self.create_indicator_tree()
        # find hierarchy
        print(self.indicator_graph)