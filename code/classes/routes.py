from .station import Station
import random
import csv
#from .network import Network

class Routes():
    def __init__(self):
        self.routes = self.get_random_routes()
        self.print_results()

    def get_random_routes(test):
        duration = 0
        stations =[]
        networks = list(test.items())
        station = random.choice(networks)
        stations.append(station)

        while duration <= 120:
            next = list(stations[-1][1].connections.items())
            next_random = random.choice(next)
            
            while True:
                for station in stations:
                    if next_random[0] == station[0]:
                        next_random = ""
                if next_random == "":
                    next_random = random.choice(next)
                elif next_random != "":
                    break

            for network in networks:
                if next_random[0] == network[0]:
                    stations.append(network)

            duration += int(next_random[1])
        return stations
    
    def print_results(self):
        """
        Method to print a csv file with results
        """
        with open('results.csv', 'w', newline='') as csvfile:
            fieldnames = ['train', 'traject']
            thewriter = csv.DictWriter(csvfile, fieldnames = fieldnames)
            thewriter.writeheader()
            trains_count = 0

            for route in self.stations:
                trains_count += 1
                thewriter.writerow({'train': trains_count, 'traject': route})


    


