class Node():
    def __init__(self, station):
        self.station = station
        self.destinations = {}

    def add_destination(self, node):
        self.destinations[node.station1] = node


        
        
