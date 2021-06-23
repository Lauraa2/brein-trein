"""
# -------------------------------------------------------------------------------
# greedy.py
# -------------------------------------------------------------------------------
#
# Creates route and routes solutions, acquired using a greedy algorithm
#
# Team de Brein Trein
#
"""

from code.classes.route import Route
from code.classes.routes import Routes

import copy
import random


class Greedy:
    """
    The Greedy class takes first the station with the fewest connections and connects the stations to the closest connections
    - The goal is to get as many routes as possible with the lowest time possible
    """
    def __init__(self, network, total_time, connections, counter):
        self.stations  = copy.deepcopy(network)
        self.copy_stations_list = list(self.stations.values())
        self.connections = connections
        self.total_time = total_time
        self.counter = counter
        self.smallest_stations = self.get_smallest_stations()
        self.used_stations = []
        self.used_connections = []
        self.get_routes()
    
    def get_smallest_stations(self):
        """
        Returns a list of all stations with the lowest number of connections.
        i.e. in the beginning it will return all stations with one connection, once those are gone all stations with two connections.
        """
        stations_connections = {}

        # iterate through all possible stations
        for station in self.copy_stations_list:
            stations_connections[station] = len(station.connections)

            # make a dictionary of all stations, sorted from few to many connections
            sorted_stations=dict(sorted(stations_connections.items(),key= lambda x:x[1], reverse=True))

        return sorted_stations

    
    def get_start_station(self):
        """
        Function to get one start station for the route
        """
        for station in self.smallest_stations:
            if station not in self.used_stations:
                self.used_stations.append(station)
                return station
            else:
                continue
    
    def get_route(self):
        """
        Function to get one route based on the stations most nearby
        """
        route = Route()
        start_station = self.get_start_station()
        route.add_station(start_station)

        while route.current_time() <= self.total_time: 
        # get the connections from the last visited station 
            current_station = route.last_station()
            possible_connections = current_station.get_connections()

            # heuristic chooses closest station as the next 
            possible_connections.sort(key=lambda a:float(a[1]))

            check_connection = True
            connection_number = 0
        
            for connection in possible_connections:
                connection_number += 1
                new_station = connection

                # for each possible connection check to see if it already is being used
                # if not, use this connection to get the next station
                if (current_station.name, connection[0]) not in self.used_connections:
                    check_connection = False
                    self.used_connections.append((current_station.name, connection[0]))
                    random_connection_name = connection[0]

                    for station in self.copy_stations_list:
                        if station.name == random_connection_name:
                            route.add_station(station)
                            break
                
                # If all random connections are already being used, choose a random one
                if connection_number == len(possible_connections) and check_connection == True:
                    check_connection = False
                    random_connection = random.choice(possible_connections)

                    for station in self.copy_stations_list:
                        if station.name == random_connection[0]:
                            route.add_station(station)
                            break

                if check_connection == False:
                    time_route = float(new_station[1])
                    route.update_time(time_route)
                    break     
    
            if route.current_time() > self.total_time:
                route.update_time(- time_route)
                route.remove_last_station()
                break         

        return route
    
    def get_routes(self):
        """
        Creates a routes solution that is filled with 
        routes that are constructed using the greedy method
        """
        counter = 0
        routes = Routes(self.connections) 

        while counter < self.counter:
            route = self.get_route()

            routes.add_route(route)
            routes.update_duration(route.duration)
            
            counter += 1
        
        routes.calculate_score()
        routes.print_results()

        return routes