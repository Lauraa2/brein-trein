from .station import Station
import csv
from .route import Route
#from .network import Network

class Routes():
    def __init__(self, routes):
        self.routes = self.add_routes(routes)
        #self.scores = self.calculate_score(routes)
    
    def add_routes(self, routes):
        """
        Method to add routes to the routes list
        """
        all_routes = []
        all_routes.append(routes)
        return all_routes
    
    #def calculate_score(self, p, counter, total_time):
        """
        Method to calculate the score from all routes
        """ 
     #   K = p*10000 - (counter*100 + total_time)
      #  self.scores.append(K)
       # return self.scores

    def print_results(new_routes):
        """
        Method to print a csv file with results
        """
        with open('results.csv', 'w', newline='') as csvfile:
            fieldnames = ['train', 'route']
            thewriter = csv.DictWriter(csvfile, fieldnames = fieldnames)
            thewriter.writeheader()
            trains_count = 0

            for key,value in new_routes.items():
                list_of_routes = []
                trains_count += 1
                for station in value.stations:
                    route = station[0]
                    list_of_routes.append(route)    
                thewriter.writerow({'train': trains_count, 'route': list_of_routes})
        

     



