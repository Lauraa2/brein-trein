from .station import Station
import random
#from .network import Network

class Routes():
    def __init__(self):
        self.routes = self.get_random_routes()

    def get_random_routes(test):
        stations =[]
        networks = list(test.items())
        station = random.choice(networks)
        stations.append(station)

        next = list(station[1].connections)

        next_random = random.choice(next)

        for network in networks:
            if next_random == network[0]:
                stations.append(network)
                print(network)

        print(station)
        print(next_random)
        print(stations)

    


