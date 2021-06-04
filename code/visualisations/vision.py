import matplotlib.pyplot as plt
import numpy as np
from code.classes import stations
import csv
 

data = []

coordinates = {}

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

     #data = [
    #   [1, 2],
    #  [3, 2],
    # [4, 7],
        #[2, 4],
        #[2, 1],
        #[5, 6],
        #[6, 3],
        #[7, 5],
    #]


    #fig, ax = plt.subplots()  # Create a figure containing a single axes.
    #ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the axes.
    #plt.show()


    #print(test)

    #N = 50
    #x = np.random.rand(N)
    #y = np.random.rand(N)

    #plt.scatter(x, y)
    #plt.show()


    #coordinatesdict = coordinates