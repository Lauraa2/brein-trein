from .station import Station
import csv
from .route import Route
#from .network import Network

class Routes():
    def __init__(self, route):
        self.stations = route
        self.routes = {}
        self.scores = []
    
    def add_routes(self, train, route):
        """
        Method to add routes to the routes dictionary
        """
        self.routes[train] = Route(route)
        return self.routes
    
    def calculate_score(self, p, counter, total_time):
        """
        Method to calculate the score from all routes
        """ 
        K = p*10000 - (counter*100 + total_time)
        self.scores.append(K)
        print(self.scores)


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



