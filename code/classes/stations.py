import csv
from .node import Node


class Station():
    def __init__(self, source_file):
        self.stations = self.load_station(source_file)
        #self.load_destination = self.load_destination(source_file)
        
    def load_station(self, source_file):
        """
        Load all the nodes into the graph.
        """
        stations = {}
        #destinations = {}
        with open(source_file, 'r') as in_file:
            reader = csv.DictReader(in_file)

            for row in reader:
                stations[row['station1'], row['station2'], row['distance']] = Node(row['station1'], row['station2'], row['distance'])
                #destinations[row['station2']] = Node(row['station1'], row['station2'])
        

        #print(stations)
        for key, value in stations.items():
            print(key[0])
            print(key[1])
            print(key[2])
            print(value)
        #print(destinations)
        
        return stations


