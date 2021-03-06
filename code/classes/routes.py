"""
# -------------------------------------------------------------------------------
# routes.py
# -------------------------------------------------------------------------------
#
# make routes objects
#
# Team de Brein Trein
#
"""

import csv


class Routes():
    def __init__(self, connections):
        '''
        routes attributes
        '''
        self.connections = connections
        self.routes = []
        self.duration = 0
        self.score = 0
    
    def add_route(self, route):
        '''
        Add route to routes
        '''
        self.routes.append(route)

    def update_duration(self, time):
        '''
        Update duration of all routes
        '''
        self.duration += time

    def remove_route(self, route):
        '''
        Remove route
        '''
        self.routes.remove(route)
    
    def calculate_fraction_connections(self):
        '''
        Calculates what fraction of the total available connections is being used
        '''
        connections_used = []

        for route in self.routes:
            for i in range(1, len(route.stations)):
                end_station = route.stations[i]
                start_station = route.stations[i - 1]
                
                check = True

                # check whether the connection created has already been completed or not, if not, add to connections
                for connection_used in connections_used:
                    if connection_used[0] == start_station.name and connection_used[1] == end_station.name:
                        check = False

                if check != False:
                    connections_used.append((start_station.name, end_station.name))
                    connections_used.append((end_station.name, start_station.name))
        
        # calculate p
        fraction = len(connections_used)/len(self.connections)

        return fraction

    def check_all_connections(self):
        '''
        Check if all available connections are being used
        '''
        if self.calculate_fraction_connections() == 1.0:
            return True

        return False
    
    def calculate_score(self):
        '''
        Method to calculate score from all routes
        '''
        counter = len(self.routes)
        p = self.calculate_fraction_connections()

        # calculate score
        self.score = float(p)*10000 - (int(counter)*100 + int(self.duration))   

        return self.score

    def print_results(self):
        '''
        Method to print a csv file with results
        '''
        with open(f'output.csv', 'w', newline='') as csvfile:
            fieldnames = ['train', 'stations']
            thewriter = csv.DictWriter(csvfile, fieldnames = fieldnames)
            thewriter.writeheader()
            trains_count = 0

            for route in self.routes:
                list_of_routes = []
                trains_count += 1

                for station in route.stations:
                    route = station.name
                    list_of_routes.append(route)

                # Ensure the printable has the appropriate format
                # Removes the quotation marks from around the names of the stations
                list_of_routes = ('[%s]' % ', '.join(map(str, list_of_routes)))    
                thewriter.writerow({'train': trains_count, 'stations': list_of_routes})

            thewriter.writerow({'train': 'score', 'stations': self.score})