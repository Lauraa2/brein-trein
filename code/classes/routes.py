from .station import Station
import csv
from .route import Route
#from .network import Network

class Routes():
    def __init__(self, route, K):
        self.stations = route
        self.score = K
        self.routes = {}
    
    def add_routes(self, train, route, K):
        """
        Method to add routes to the routes dictionary
        """
        self.routes[train, K] = Route(route)
        print(self.routes)
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



