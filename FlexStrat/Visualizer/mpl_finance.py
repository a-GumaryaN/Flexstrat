from .Visualizer_abstraction import Visualizer_abstraction
import mplfinance as mpf
import matplotlib.pyplot as plt
from time import sleep

class MPL_visualizer(Visualizer_abstraction):

    def initialize(self):
        self._visualizer_name = "MPL visualizer"
        self.width = 10
        self.height = 6
        if width in self.config:
            width = self.config["width"]
        if height in self.config:
            height = self.config["height"]
        self.fig, self.axes = mpf.plot(self.shared_data["candles"], 
                        type='candle', 
                        style='charles',
                        returnfig=True,
                        figsize=(self.width, self.height))

    def run(self):
        while True :
            self.axes[0].clear()
            self.fig, self.axes = mpf.plot(self.shared_data["candles"], 
                        type='candle', 
                        style='charles',
                        returnfig=True,
                        figsize=(self.width, self.height))
            plt.draw()
            plt.pause(0.01)
            sleep(self.config["display_delay"])