import matplotlib.pyplot as plt
import numpy as np
#from code.classes import stations
import csv

#N = 50
#x = np.random.rand(N)
#y = np.random.rand(N)

#plt.scatter(x, y)
#plt.show()

#coordinates = {}

#with open('data/StationsHolland.csv', 'r') as in_file:
#    reader = csv.DictReader(in_file)

#    for row in reader:
#        coordinates[row['station']] = [row['x'], row['y']]

#coordinatesdict = coordinates
#data = []

#for value in coordinatesdict.values():
#    data.append(value)

#print(data)

data = [
    [1, 2],
    [3, 2],
    [4, 7],
    [2, 4],
    [2, 1],
    [5, 6],
    [6, 3],
    [7, 5],
]

x, y = zip(*data)
plt.scatter(x, y)
plt.show()


#fig, ax = plt.subplots()  # Create a figure containing a single axes.
#ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the axes.
#plt.show()