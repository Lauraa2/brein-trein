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

<<<<<<< HEAD
    def load_destinations(self, source_file):
        """
        Load all the neighbours into the loaded nodes.
=======
    def load_destination(self, source_file):
        """
        Load all the destinations into the loaded nodes.
>>>>>>> 8c59e1ba16dd1116cec9a770679b63211e5c9414
        """
        with open(source_file, 'r') as in_file:
            reader = csv.DictReader(in_file)

            for row in reader:
                destinations = []
                destinations.append(row['station2'])
<<<<<<< HEAD

                #print(destinations)

                #node_id = row['id']
                station1 = row['station1']
=======
                
                print(destinations)

                station1 = row['station1']

                # Add the destination to the correct node
                for destination in destinations:
                    destination = self.stations[destination]
                    self.stations[station1].add_destination(destination)
>>>>>>> 8c59e1ba16dd1116cec9a770679b63211e5c9414

                # Add the neighbours to the correct node
                for neighbour in neighbours:
                    neighbour = self.nodes[neighbour]
                    self.nodes[node_id].add_neighbour(neighbour)