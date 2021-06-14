from .station import Station
import csv
from .route import Route
#from .network import Network

class Routes():
    def __init__(self, routes, duration, connections):
        self.routes = routes
        self.duration = duration
        self.connections = connections
        self.score = self.calculate_score()
        self.print_results()
    
    def calculate_score(self):
        """
        Method to calculate the score from all routes
        """ 
        counter = len(self.routes)
        connections_used = []

        for route in self.routes:
            for i in range(1, len(route.route)):
                end_station = route.route[i]
                start_station = route.route[i - 1]
                check = True

        # check of de gemaakte verbinding al is bereden of niet, zo nee, voeg toe aan verbindingen
                for connection_used in connections_used:
                    if connection_used[0] == start_station[0] and connection_used[1] == end_station[0]:
                        check = False

                if check != False:
                    connections_used.append((start_station[0], end_station[0]))
        
        # bereken p
        p = len(connections_used)/len(self.connections)

        # bereken score
        score = float(p)*10000 - (int(counter)*100 + int(self.duration))
        print(score)
        return score

    def print_results(self):
        """
        Method to print a csv file with results
        """
        with open('output.csv', 'w', newline='') as csvfile:
            fieldnames = ['train', 'route']
            thewriter = csv.DictWriter(csvfile, fieldnames = fieldnames)
            thewriter.writeheader()
            trains_count = 0

            for route in self.routes:
                list_of_routes = []
                trains_count += 1
                for station in route.route:
                    route = station[0]
                    list_of_routes.append(route)    
                thewriter.writerow({'train': trains_count, 'route': list_of_routes})
            thewriter.writerow({'train': 'score:', 'route': self.score})
        

     



