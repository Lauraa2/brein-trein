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

        while duration <= 120:
            next = list(stations[-1][1].connections.items())
            next_random = random.choice(next)

            for station in stations: 
                while next_random[0] == station[0]:
                    if len(next) >= 2:
                        next_random = random.choice(next)
                    else:
                        next_random = next[0]
                        break

            for network in networks:
                if next_random[0] == network[0]:
                    stations.append(network)

            duration += int(next_random[1])
           
        print(stations)

    


