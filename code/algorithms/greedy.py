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

        #print(self.connections)

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
        print(" ")
        print(self.smallest_stations)
        print(" ")
        for station in self.smallest_stations:
            if station not in self.used_stations:
                print("x")
                print(station.connections)
                print("x")
                self.used_stations.append(station)
                return station
            #elif station in self.used_stations:
            else:
                continue
    
    def get_route(self):
        """
        Function to get one route based on the stations most nearby
        """
        route = Route()
        start_station = self.get_start_station()
        print("z")
        print(start_station)
        print("z")
        route.add_station(start_station)

        while route.current_time() <= self.total_time:
        # Get the connections from the currently last visited station (E)
            current_station = route.last_station()
            print("a")
            print(current_station)
            print("a")
            possible_connections = current_station.get_connections()

            print('c')
            print(possible_connections)
            print('c')

            # Heuristic chooses closest station as the next (E)
            possible_connections.sort(key=lambda a:float(a[1]))
        
            for connection in possible_connections:
                print('b')
                print(connection[0])
                print('b')
                new_station = connection
                if (current_station.name, connection[0]) not in self.used_connections:
                    print('hallo')
                    print(current_station.name)
                    print(connection[0])
                    self.used_connections.append((current_station.name, connection[0]))
                    print("x x")
                    print(self.used_connections)
                    print("x x")
                    #current_station = connection
                    random_connection_name = connection[0]
                    for station in self.copy_stations_list:
                        if station.name == random_connection_name:
                            route.add_station(station)
                else:
                    check_connection = True
                    for used_connection in self.used_connections:
                        if used_connection[0] == current_station.name and used_connection[1] == connection[0]:
                            #print("same")
                            check_connection = False
                            
                            break
                    if check_connection == True or len(possible_connections) == 1:
                        self.used_connections.append((current_station.name, connection[0]))
                        new_station = connection
                        station_name = new_station[0]
                        for station in self.copy_stations_list:
                            if station.name == station_name:
                                route.add_station(station)
                                break
                    '''
                    new_station = connection
                    station_name = new_station[0]
                    for station in self.copy_stations_list:
                        if station.name == station_name:
                            route.add_station(station)
                            break
                    time_route = float(new_station[1])
                    print(time_route)
                    route.update_time(time_route)
                    break   
      
        
                else:
                    check_connection = True
                    for used_connection in self.used_connections:
                        if used_connection[0] == current_station.name and used_connection[1] == connection[0]:
                            #print("same")
                            check_connection = False
                            if len(possible_connections) >= 2:
                                possible_connections.remove(connection)
                            break
                    if check_connection == True or len(possible_connections) == 1:
                        self.used_connections.append((current_station.name, connection[0]))
                        new_station = connection
                        station_name = new_station[0]
                        for station in self.copy_stations_list:
                            if station.name == station_name:
                                route.add_station(station)
                                break
                    '''
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