class Node():
<<<<<<< HEAD
<<<<<<< HEAD
    def __init__(self, name, station1):
        self.name = name
        self.station1 = station1
=======
    def __init__(self, station1, station2, distance):
        self.station1 = station1
        self.station2 = station2
        self.distance = distance
>>>>>>> 7e32acd85d56d10e61597008c605cc35cd5130f8
        self.destinations = {}
        self.value = None

    def add_destination(self, node):
        self.destinations[node.station1] = node
=======
    def __init__(self, station):
        self.station = station

    def add_destination(self, station):
        self.destinations[station.station1] = station
    
    def add_distance(self, station):
        self.distances[station.station1] = station
>>>>>>> 05fd63d43c15015eb847d509efb4799377cc762b
       


        
        
