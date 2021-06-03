import csv
from .node import Node



class Station():
    def __init__(self, source_file):
        self.station = self.load_station(source_file)
        
    def load_station(self, source_file):
        """
        Load all the nodes into the graph.
        """
        stations = {}
        with open(source_file, 'r') as in_file:
            reader = csv.DictReader(in_file)

            for row in reader:
                stations[row['station1']] = Node(row['station1'])

        print(stations)

    