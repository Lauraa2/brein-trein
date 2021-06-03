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
                stations[row['station1']] = Node(row['station1'], row['station1'])

        print(stations)
        
        return stations

    def load_destinations(self, source_file):
        """
        Load all the neighbours into the loaded nodes.
        """
        with open(source_file, 'r') as in_file:
            reader = csv.DictReader(in_file)

            for row in reader:
                destinations = []
                destinations.append(row['station2'])

                #print(destinations)

                #node_id = row['id']
                station1 = row['station1']

                # Add the neighbours to the correct node
                for neighbour in neighbours:
                    neighbour = self.nodes[neighbour]
                    self.nodes[node_id].add_neighbour(neighbour)