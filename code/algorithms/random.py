import random
from code.classes.routes import Routes
import copy

def get_random_routes(test):
        routes = {}
        counter = 0
        while len(routes) < 7:
            duration = 0
            stations =[]
            copy_stations = copy.deepcopy(test)
            networks = list(copy_stations.items())
            station = random.choice(networks)
            stations.append(station)

            while duration <= 120:
                next = list(stations[-1][1].connections.items())
                next_random = random.choice(next)

                for station in stations: 
                    while next_random[0] == station[0]:
                        next_random = random.choice(next)
                        break

                for network in networks:
                    if next_random[0] == network[0]:
                        stations.append(network)

                duration += int(next_random[1])

                if duration >= 120:
                    counter += 1
                    routes[counter] = Routes(stations)
                    routes[counter].add_routes(counter, stations)
                    break

        print(counter)
        print(routes)

        return routes