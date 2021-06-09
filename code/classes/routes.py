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

def print_results(routes_random):
    """
    Method to print a csv file with results
    """
    with open('results.csv', 'w', newline='') as csvfile:
        fieldnames = ['train', 'route']
        thewriter = csv.DictWriter(csvfile, fieldnames = fieldnames)
        thewriter.writeheader()
        trains_count = 0
        
        for key,value in routes_random.items():
            routes = []
            trains_count += 1
            for station in value.stations:
                route = station[0]
                routes.append(route)    
            thewriter.writerow({'train': trains_count, 'route': routes})


