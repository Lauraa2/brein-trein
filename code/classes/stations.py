import csv
from .node import Node


class Station():
    def __init__(self, source_file):
        self.stations = self.load_station(source_file)
        
    def load_station(self, source_file):
        """
        Load all the stations
        """
        stations = {}
        coordinates = {}

        with open(source_file, 'r') as in_file:
            reader = csv.DictReader(in_file)

            for row in reader:
                stations[row['station']] = Node(row['station'])

                coordinates[row['x']] = Node(row['x'])
                coordinates[row['y']] = Node(row['y'])

        

        #print(coordinates)
  
        return stations


