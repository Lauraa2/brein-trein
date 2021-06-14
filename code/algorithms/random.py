import random
from code.classes.routes import Routes
from code.classes.route import Route
import copy
          
def get_random_route(network, connections, total_time):
    """
    Function to get one random route
    - Time per route is less than 2 hours
    """
    # kopieer de stations en stop ze in een lijst zodat we een random object kunnen vinden
    copy_stations = copy.deepcopy(network)
    copy_stations_list = list(copy_stations.items())

    # maak een lege lijst aan voor stations 
    stations = []

    # pak een random station uit de lijst met stationnetjes
    start_station = random.choice(copy_stations_list) # geeft een random object ('Amsterdam Centraal', <code.classes.station.Station object at 0x7fd015d33310>)

    # voeg het station toe aan een lijst die de connecties gaat laden 
    stations.append(start_station)

    # zet de tijd op 0 voor een nieuw traject
    time = 0

    while time <= total_time:
        
        # pak het laatst toegevoegde station uit de lijst als nieuw station
        connections_start_station = list(stations[-1][1].connections.items())
        random_connection = random.choice(connections_start_station)
        new_station = stations[-1][0]

        #print(stations)
        for station in stations:
            if random_connection[0] == station[0]:
                print(random_connection[0])
                print(station[0])
                if len(connections_start_station) >= 2:
                    connections_start_station.remove(random_connection)
                    random_connection = random.choice(connections_start_station)
                else:
                    connections_start_station

        random_connection_name = random_connection[0]

        time_route = float(random_connection[1])

        # add the station object of the connection to the stations list
        for station in copy_stations_list:
            if station[0] == random_connection_name:
                stations.append(station)
            
        # update de totale tijd van de route
        time += time_route

        # update het aantal routes
        if time == total_time:
            route = Route(stations, time)
            return route
        elif time > total_time:
            # verwijder het laatste station uit de lijst, zodat de tijd niet over 120 of 180 gaat
            time -= time_route
            stations.pop()
            route = Route(stations, time)
            return route

def get_random_routes(network, connections, total_time, total_counter):
    """
    random function to get max seven routes
    """
    counter = 0
    routes = []
    duration = 0
    while counter < total_counter:
        route = get_random_route(network, connections, total_time)
        routes.append(route)
        counter += 1
        duration += route.duration

        if counter == total_counter:
            new_routes = Routes(routes, duration, connections)
            return new_routes
