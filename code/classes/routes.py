from .station import Station
import random
#from .network import Network

class Routes():
    def __init__(self):
        self.routes = self.get_random_station()

    def get_random_station(test):
        stations =[]
        networks = list(test.items())
        station = random.choice(networks)
        stations.append(station)

        next = list(station[1].connections)

        next_random = random.choice(next)
        stations.append(next_random)

        print(station)
        print(next_random)
        print(stations)

    #def add_random_station(self, start):
     #   self.stations.append(start)


