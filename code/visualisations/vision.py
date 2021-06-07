import matplotlib.pyplot as plt
import numpy as np
from code.classes import network
import csv

coordinates = {}
data = []

def print_stations():
    for station in network:
        print(station.x)
    
with open('data/StationsHolland.csv', 'r') as in_file:
    reader = csv.DictReader(in_file)

    for row in reader:
        coordinates[row['station']] = [float(row['x']), float(row['y'])]


    for value in coordinates.values():
        data.append(value)

    y, x = zip(*data)
    plt.ylim(51.5, 53)
    plt.xlim(4.2, 5)
    plt.scatter(x, y)
    plt.savefig("plot.png")
    plt.show()