import matplotlib.pyplot as plt
import numpy as np
from code.classes import network
from code.classes import routes
from code.algorithms import random
import csv

coordinates = []

data = []

trajecten = []

dictionary = {}

def print_stations(network, routes):
    """
    Function to visualize the routes
    """

    for key,value in routes.items():
        trajecten.append(value.stations)
        
    for key,value in network.items():
        dictionary[key] = [float(value.x), float(value.y)]

    for traject in trajecten:
        for station in traject:
            if station in dictionary:
                data.append(dictionary[station])

        y, x = zip(*data)
        plt.ylim(51.5, 53)
        plt.xlim(4.2, 5.2)
        plt.plot(x, y, '-ok')
        plt.savefig("plot.png")
        plt.show()