import random
from code.classes.routes import Routes
from code.classes.route import Route
import copy
          
def get_random_route(network, total_time):
    # kopieer de stations en stop ze in een lijst zodat we een random object kunnen vinden
    copy_stations = copy.deepcopy(network)
    # dit volgende heb ik veranderd naar een lijst met alleen objecten in plaats van ook namen (namen zit al in het object)
    copy_stations_list = list(copy_stations.values())

    # Initiate a route object (E)
    route = Route()

    # pak een random station uit de lijst met stationnetjes
    start_station = random.choice(copy_stations_list) # geeft een random object ('Amsterdam Centraal', <code.classes.station.Station object at 0x7fd015d33310>)

    # Add starting station to route (E)
    route.add_station(start_station)

    while route.current_time() <= total_time:
        # Get the connections from the currently last visited station (E)
        current_station = route.last_station()
        possible_connections = current_station.get_connections()

        # Heuristic chooses closest station as the next (E)
        possible_connections.sort(key=lambda a:float(a[1]))
        new_station = possible_connections[0]

        for connection in possible_connections: # this I did slightly different (tuples instead of dict) (E)
            if connection == new_station[0]:
                del connection 

        # Choose a random connection that is not already present in the route (E)

        random_connection = random.choice(possible_connections)
        if route.check_station(random_connection[0]) and len(possible_connections) >= 2:
            possible_connections.remove(random_connection)
        
        random_connection_name = random_connection[0]

        time_route = float(random_connection[1])

        # add the station object of the connection to the stations list
        for station in copy_stations_list:
            if station.name == random_connection_name:
                route.add_station(station)
            
        # update de totale tijd van de route
        route.update_time(time_route)
    
        # Check whether the duration does not exceed the maximum time
        if route.current_time() > total_time:
            route.update_time(- time_route)
            route.remove_last_station()
            break

    return route

def get_random_routes(network, connections, total_time, total_counter):
    counter = 0
    routes = Routes(connections) 

    while counter < total_counter:
        route = get_random_route(network, total_time)

        routes.add_route(route)
        routes.update_duration(route.duration)
        
        counter += 1

    return routes
