import matplotlib.pyplot as plt
import numpy as np
from code.classes import network
from code.classes import routes
from code.algorithms import random
import random

from collections import defaultdict
import csv

data = []
trajecten = []
dictionary = {}
trein = {}

def print_stations(test, test2):
    
    for key,value in test2.items():
        trajecten.append(value.stations)
        
    for key,value in test.items():
        dictionary[key] = [float(value.x), float(value.y)]
        

    k = 0
    for traject in trajecten:
        data = []
        for station in traject:
            if station[0] in dictionary:
                data.append(dictionary[station[0]])

        trein[k] = data

        for k in trein:
            y, x = zip(*data) 
            plt.plot(x, y, '-o')

        k += 1

    plt.ylim(51.5, 53)
    plt.xlim(4.2, 5.2)
    plt.savefig("plot.png")
    plt.show()



