from .station import Station
import random
#from .network import Network

class Routes():
    def __init__(self):
        self.routes = self.get_random_routes()

    def get_random_routes(test):
        duration = 0
        stations =[]
        networks = list(test.items())
        station = random.choice(networks)
        stations.append(station)

        next = list(station[1].connections.items())
        print(next)

        next_random = random.choice(next)

        for network in networks:
            if next_random == network[0]:
                stations.append(network)
                print(network)

        duration += int(next_random[1])

        print(duration)

        print(station)
        print(next_random)
        print(stations)

    


