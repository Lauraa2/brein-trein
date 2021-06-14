from .station import Station
import csv
from .route import Route
#from .network import Network

class Routes():
    def __init__(self, routes, duration, connections):
        self.routes = routes
        self.duration = duration
        self.connections = connections
        self.scores = self.calculate_score()
    
    def add_routes(self, routes):
        """
        Method to add routes to the routes list
        """
        all_routes = routes
        return all_routes
    
    def calculate_score(self):
        """
        Method to calculate the score from all routes
        """ 
        counter = len(self.routes)
        connections_used = []
        check = True

        for route in self.routes:
            print(route.route)
            for station in route.route:
                print(station[0])

        # check of de gemaakte verbinding al is bereden of niet, zo nee, voeg toe aan verbindingen
                for connection_used in connections_used:
                    if connection_used[0] == station[0] and connection_used[1] == station[1]:
                        check = False
                        break

        if check != False:
            connections_used.append((new_station, random_connection_name))
            time_route = int(random_connection[1])
        
        #K = p*10000 - (counter*100 + total_time)
        #self.scores.append(K)
        #return self.scores

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
        

     



