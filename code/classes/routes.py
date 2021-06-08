from .station import Station
import csv
#from .network import Network

class Routes():
    def __init__(self, stations):
        self.stations = stations
        self.routes = {}
        self.print_results()
    
    def add_routes(self, train, stations):
        self.routes[train] = stations
        print(self.routes)

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
    


