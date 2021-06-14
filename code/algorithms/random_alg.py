import random
from code.classes.routes import Routes
from code.classes.route import Route
import copy
          
def get_random_route(network, connections):
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

    while time <= 120:
        
        # pak het laatst toegevoegde station uit de lijst als nieuw station
        connections_start_station = list(stations[-1][1].connections.items())
        random_connection = random.choice(connections_start_station)
        new_station = stations[-1][0]

        random_connection_name = random_connection[0]

        time_route = int(random_connection[1])

        # add the station object of the connection to the stations list
        for station in copy_stations_list:
            if station[0] == random_connection_name:
                stations.append(station)
            
        # update de totale tijd van de route
        time += time_route

        # update het aantal routes
        if time == 120:
            route = Route(stations, time)
            return route
        elif time > 120:
            # verwijder het laatste station uit de lijst, zodat de tijd niet over 120 gaat
            time -= time_route
            stations.pop()
            route = Route(stations, time)
            return route

def get_random_routes(network, connections):
    """
    random function to get max seven routes
    """
    counter = 0
    routes = []
    duration = 0
    while counter < 7:
        route = get_random_route(network, connections)
        routes.append(route)
        counter += 1
        duration += route.duration

        if counter == 7:
            new_routes = Routes(routes, duration, connections)
            return new_routes