import copy
import random
from code.classes.route import Route
from code.classes.routes import Routes

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

        # Iterate through all possible stations
        for station in self.copy_stations_list:
            stations_connections[station] = len(station.connections)

            # Make a dictionary of all stations, sorted from few to many connections
            sorted_stations=dict(sorted(stations_connections.items(),key= lambda x:x[1]))

        return sorted_stations
    
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
        check = False

        while route.current_time() <= self.total_time:
        # Get the connections from the currently last visited station (E)
            current_station = route.last_station()
            possible_connections = current_station.get_connections()

            # Heuristic chooses closest station as the next (E)
            possible_connections.sort(key=lambda a:float(a[1]))
            print(possible_connections)
            for connection in possible_connections:
                if self.used_connections == []:
                    self.used_connections.append((current_station.name, connection))
                    new_station = connection
                    station_name = new_station[0]
                    check == True
                    break
        
                else:
                    for used_connection in self.used_connections:
                        if used_connection[0] != current_station.name and used_connection[1] != connection[0] or len(possible_connections) >= 1:
                            self.used_connections.append((current_station.name, connection))
                            new_station = connection
                            station_name = new_station[0]
                            check == True
                            print(station_name)
                            break
            
                if check != True:
                    continue
    
                
            for station in self.copy_stations_list:
                if station.name == station_name:
                    route.add_station(station)
            
            time_route = float(new_station[1])
            route.update_time(time_route)
            if route.current_time() > self.total_time:
                route.update_time(- time_route)
                route.remove_last_station()
                break         

        return route
    
    def get_routes(self):
        counter = 0
        routes = Routes(self.connections) 

        while counter < self.counter:
            route = self.get_route()

            routes.add_route(route)
            routes.update_duration(route.duration)
            
            counter += 1
        
        score = routes.calculate_score()
        print(score)
        routes.print_results()

        return routes

            
            
            
