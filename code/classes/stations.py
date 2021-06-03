import csv
from .node import Node


class Station():
    def __init__(self, source_file):
        self.stations = self.load_station(source_file)
        self.load_destination = self.load_destination(source_file)
        
    def load_station(self, source_file):
        """
        Load all the nodes into the graph.
        """
        stations = {}
        with open(source_file, 'r') as in_file:
            reader = csv.DictReader(in_file)

            for row in reader:
                stations[row['station1']] = Node(row['station1'], row['station2'])
        
        print(stations)
        
        return stations

    def load_destination(self, source_file):
        """
        Load all the destinations into the loaded nodes.
        """
        with open(source_file, 'r') as in_file:
            reader = csv.DictReader(in_file)

            for row in reader:
                destinations = []
                destinations.append(row['station2'])
                
                print(destinations)

                station1 = row['station1']

                # Add the destination to the correct node
                for destination in destinations:
                    destination = self.stations[destination]
                    self.stations[station1].add_destination(destination)

    