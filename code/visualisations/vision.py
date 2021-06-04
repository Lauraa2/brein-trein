import matplotlib.pyplot as plt
import numpy as np
from code.classes import stations
import csv

coordinates = {}
data = []

with open('data/StationsHolland.csv', 'r') as in_file:
    reader = csv.DictReader(in_file)

    for row in reader:
        coordinates[row['station']] = [float(row['x']), float(row['y'])]


    for value in coordinates.values():
        data.append(value)

    x, y = zip(*data)
    print(x)

    plt.xlim(50, 53)
    plt.ylim(3, 5)
    plt.scatter(x, y)
    plt.show()