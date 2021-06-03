
class Node():
    def __init__(self, name, station1):
        self.name = name
        self.station1 = station1
        self.destinations ={}
        self.value = None

    def add_destination(self, node):
        self.destinations[node.station1] = node
        
        
