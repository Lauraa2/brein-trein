import csv

from collections import defaultdict

class Location():
    def __init__(self, source_file):
        self.location = self.load_location(source_file)
        
    def load_location(self, source_file):
        """
        Load all the nodes into the graph.
        """
        location = {}

        with open(source_file, 'r') as in_file:
            reader = csv.DictReader(in_file)

            for row in reader:
                location[row['station'], row['y'], row['x']] = coordinates(row['station'], row['y'], row['x'])
                #location[index].append(coordinates(row['station'], row['y'], x = row['x']))

        #print(location)

        

"""
def get_location(self, index):
        
        Returns the transmitters of a specific location.
        
        if index in self.location:
            return self.location[index]

        raise KeyError("Location does not exist.")
"""


class coordinates():
    """
    Dataclass containing transmitter info.
    """
    def __init__(self, station, x, y):
        self.station = station
        self.x = x
        self.y = y