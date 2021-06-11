import matplotlib.pyplot as plt
import numpy as np
from code.classes import network
from code.classes import routes
from code.algorithms import random
import random
import csv

coordinates = []
data = []
trajecten = []
dictionary = {}

def print_stations(test, test2):

    for key,value in test2.items():
        trajecten.append(value.stations)

    for key,value in test.items():
        dictionary[key] = [float(value.x), float(value.y)]

    colors = ['red', 'green', 'blue', 'yellow', 'grey', 'black', 'purple', 'pink']
    
    for i in colors:
        random_color = random.choice(colors)
        colors.remove(random_color)


    k = 0
    for traject in trajecten:
        k += 1
        for station in traject:
            if station[0] in dictionary:
                data.append(dictionary[station[0]])
    
        y, x = zip(*data)
        plt.ylim(51.5, 53)
        plt.xlim(4.2, 5.2)
        plt.plot(x, y, '-o', color='black')
        plt.savefig("plot.png")
        plt.show()