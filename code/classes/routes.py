from .station import Station
import random
#from .network import Network

class Routes():
    def __init__(self):
        self.routes = self.get_random_routes()

    def get_random_routes(test):
        #counter = 0
        #while counter <= 100:
        duration = 0
        #counter = 0
        stations =[]
        networks = list(test.items())
        station = random.choice(networks)
        stations.append(station)

        while duration <= 120:
            #if counter <= 7:
            next = list(stations[-1][1].connections.items())
                #print(next)
            next_random = random.choice(next)
            #print(next_random[0])

            #print(stations[0])

            for station in stations: 
                while next_random[0] == station[0]:
                    #print(station[0])
                    #next.remove(next_random)
                    #print(next)
                    if len(next) >= 2:
                        next_random = random.choice(next)
                    else:
                        next_random = next[0]
                        #print(next_random)

            for network in networks:
                if next_random[0] == network[0]:
                    stations.append(network)

            duration += int(next_random[1])
        #counter += 1

        #print(duration)
        print(stations)

    


