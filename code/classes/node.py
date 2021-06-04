class Node():
    def __init__(self, station):
        self.station = station
        self.connections = {}

    def add_connection(self, station):
        self.connections[station.station] = station

    def add_destination(self, station):
        self.destinations[station.station1] = station
    
    def add_distance(self, station):
        self.distances[station.station1] = station
       


        
        
