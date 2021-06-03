
class Node():
    def __init__(self, station1, station2):
        self.station1 = station1
        self.station2 = station2
        self.destinations = {}

    def add_destination(self, node):
        self.destinations[node.station1] = node
       


        
        
