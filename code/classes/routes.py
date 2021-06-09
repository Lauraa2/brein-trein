from .station import Station
import csv
#from .network import Network

class Routes():
    def __init__(self, stations):
        self.stations = stations
        self.routes = {}
    
    def add_routes(self, train, stations):
        """
        Method to add routes to the routes dictionary
        """
        self.routes[train] = stations
        return self.routes

def print_results(test2):
    """
    Method to print a csv file with results
    """
    with open('results.csv', 'w', newline='') as csvfile:
        fieldnames = ['train', 'route']
        thewriter = csv.DictWriter(csvfile, fieldnames = fieldnames)
        thewriter.writeheader()
        trains_count = 0

        print(test2)
        
        
        #for key,value in test2.items():
        for key,value in test2.items():
            routess = []
            print(value.stations)
            trains_count += 1
            for station in value.stations:
                route = station
                routess.append(route)    
            thewriter.writerow({'train': trains_count, 'route': routess})


