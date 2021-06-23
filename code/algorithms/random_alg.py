"""
# -------------------------------------------------------------------------------
# greedy.py
# -------------------------------------------------------------------------------
#
# Croutes a random route or routes solution
# Always uses the maximum amount of routes and minutes per route
#
# Team de Brein Trein
#
"""

from code.classes.routes import Routes
from code.classes.route import Route

import copy
import random
          
def get_random_route(network, total_time):
    """
    Retrieve a route within maximum amount of time following random connections
    """
    copy_stations = copy.deepcopy(network)
    copy_stations_list = list(copy_stations.values())

    route = Route()

    start_station = random.choice(copy_stations_list) 
    route.add_station(start_station)

    while route.current_time() <= total_time:
        # get the connections from the currently last visited station
        current_station = route.last_station()
        possible_connections = current_station.get_connections()

        # choose a random connection that is not already present in the route 
        random_connection = random.choice(possible_connections)
        if route.check_station(random_connection[0]) and len(possible_connections) >= 2:
            possible_connections.remove(random_connection)
        
        random_connection_name = random_connection[0]

        time_route = float(random_connection[1])

        # add the station object of the next station to the stations list
        for station in copy_stations_list:
            if station.name == random_connection_name:
                route.add_station(station)
            
        route.update_time(time_route)
    
        # check whether the duration does not exceed the maximum time
        if route.current_time() > total_time:
            route.update_time(- time_route)
            route.remove_last_station()
            break

    return route

def get_random_routes(network, connections, total_time, total_counter):
    """
    Create a routes solution using the maximum amount of routes
    The routes are created at random
    """
    counter = 0
    routes = Routes(connections) 

    while counter < total_counter:
        route = get_random_route(network, total_time)

        routes.add_route(route)
        routes.update_duration(route.duration)
        
        counter += 1

    routes.calculate_score()
    routes.print_results()
    
    return routes
