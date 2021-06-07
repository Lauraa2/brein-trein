from .station import Station
import random
#from .network import Network

class Routes():
    def __init__(self, start, destination, duration):
        self.start = start
        self.destination = destination
        self.duration = int(duration)
        
        self.stations = []
        self.get_random_station()

    def get_random_station(test):
        entry_list = list(test.items())
        station = random.choice(entry_list)
        stations.append(station)
      
        print(stations)

    #def add_random_station(self, start):
     #   self.stations.append(start)


