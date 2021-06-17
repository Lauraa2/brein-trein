import copy
import random
from code.classes.route import Route

class Greedy:
    """
    The Greedy class takes first the station with the fewest connections and connects the stations to the closest connections
    - The goal is to get as many routes as possible with the lowest time possible
    """
    def __init__(self, network, total_time):
        self.stations  = copy.deepcopy(network)
        self.copy_stations_list = list(self.stations.values())
        self.total_time = total_time
        self.smallest_stations = self.get_smallest_stations()
        self.used_stations = []
        self.get_route()
    
    def get_smallest_stations(self):
        """
        Returns a list of all stations with the lowest number of connections.
        i.e. in the beginning it will return all stations with one connection, once those are gone all stations with two connections.
        """
        smallest_stations = []

        # Iterate through all possible stations
        for station in self.copy_stations_list:
            # Add the station to the list if the list is empty
            smallest_stations.append(station)
            
            #elif not smallest_stations:
                #smallest_stations.append(station)
            # Replace the list if the current station has less connections than the stations currently in the list
            if len(station.connections) < len(smallest_stations[-1].connections):
                smallest_stations.clear()
                smallest_stations.append(station)
            # If the current station has as many connections as the stations already in the list, add it
            elif len(station.connections) == len(smallest_stations[0].connections):
                smallest_stations.append(station)
        return smallest_stations
    
    def get_start_station(self):
        """
        Function to get one start station for the route
        """
        for station in self.smallest_stations:
            if station not in self.used_stations:
                self.used_stations.append(station)
                return station
            elif station in self.used_stations:
                continue
    
    def get_route(self):
        """
        Function to get one route based on the stations most nearby
        """
        route = Route()
        start_station = self.get_start_station()
        route.add_station(start_station)

        while route.current_time() <= self.total_time:
        # Get the connections from the currently last visited station (E)
            current_station = route.last_station()
            print(current_station)
            possible_connections = current_station.get_connections()

            # Heuristic chooses closest station as the next (E)
            possible_connections.sort(key=lambda a:float(a[1]))
            print(possible_connections)
            for station in possible_connections:
                if station not in self.used_stations:
                    new_station = station
                    self.used_stations.append(new_station)
                    no_station = False
                    break
            
            if no_station != False:
                new_station = random.choice(possible_connections)

            print(new_station)
            
            station_name = new_station[0]

            time_route = float(new_station[1])

            # add the station object of the connection to the stations list
            for station in self.copy_stations_list:
                if station.name == station_name:
                    route.add_station(station)

            # update the time of the route with the added station        
            route.update_time(time_route)
    
            # Check whether the duration does not exceed the maximum time
            if route.current_time() > self.total_time:
                route.update_time(- time_route)
                route.remove_last_station()
                break

        return route
    
    def get_routes(network, connections, total_time, total_counter):
    counter = 0
    routes = Routes(connections) 

    while counter < total_counter:
        route = self.get_route(network, total_time)

        routes.add_route(route)
        routes.update_duration(route.duration)
        
        counter += 1

    return routes

            
            
            
