import matplotlib.pyplot as plt
import numpy as np
from code.classes import network
import csv

#coordinates = {}
data = []

def print_stations(test):

    for key,value in test.items():
        #print("Key : {} , Value : {}".format(key,value.x))
        data.append([float(value.x), float(value.y)])
       
    #print(data)

    y, x = zip(*data)
    plt.ylim(51.5, 53)
    plt.xlim(4.2, 5)
    plt.scatter(x, y)
    plt.savefig("plot.png")
    plt.show()