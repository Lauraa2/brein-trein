
class Node():
    def __init__(self, station1, station2, distance):
        self.station1 = station1
        self.station2 = station2
        self.distance = distance
        self.destinations = {}
        self.distances = {}

    def add_destination(self, station):
        self.destinations[station.station1] = station
    
    def add_distance(self, station):
        self.distances[station.station1] = station
       


        
        
