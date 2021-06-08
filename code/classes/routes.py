from .station import Station
import random
import csv
#from .network import Network

class Routes():
    def __init__(self):
        self.routes = self.get_random_routes()
        self.print_results()

    def get_random_routes(test):
        stack = [""]
        #counter = 0
        #while counter <= 100:
        while len(stack) > 0:
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
        print(stations)
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


        


