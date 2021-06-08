from .station import Station
import random
import csv
#from .network import Network

class Routes():
    def __init__(self):
        self.routes = self.get_random_routes()
        self.print_results()

    def get_random_routes(test):
        routes = {}
        counter = 0
        while len(routes) < 7:
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
                        next_random = random.choice(next)
                        break

                for network in networks:
                    if next_random[0] == network[0]:
                        stations.append(network)

                duration += int(next_random[1])

                if duration >= 120:
                    counter += 1
                    routes[counter] = stations
                    break

        print(counter)
        print(routes)

        return routes
    
    def print_results(self):
        """
        Method to print a csv file with results
        """
        with open('results.csv', 'w', newline='') as csvfile:
            fieldnames = ['train', 'traject']
            thewriter = csv.DictWriter(csvfile, fieldnames = fieldnames)
            thewriter.writeheader()
            trains_count = 0

            for route in self.routes.values():
                trains_count += 1
                thewriter.writerow({'train': trains_count, 'traject': route})


        


