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
    copy_connections = copy.deepcopy(connections)

    # maak een lijst voor alle bereden verbindingen
    connections_used = []

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

        check = True

        # check of de gemaakte verbinding al is bereden of niet, zo nee, voeg toe aan verbindingen
        for connection_used in connections_used:
            if connection_used[0] == new_station and connection_used[1] == random_connection_name:
                check = False
                break

        if check != False:
            connections_used.append((new_station, random_connection_name))
            time_route = int(random_connection[1])

        # add the station object of the connection to the stations list
        for station in copy_stations_list:
            if station[0] == random_connection_name:
                stations.append(station)
            
        # update de totale tijd van de route
        time += time_route

        # update het aantal routes
        if time == 120:
            route = Route(stations)
            return route
        elif time > 120:
            # verwijder het laatste station uit de lijst, zodat de tijd niet over 120 gaat
            time -= time_route
            stations.pop()
            route = Route(stations)
            return route


def get_random_routes(network, connections):
    """
    random function to get max seven routes
    """
    counter = 0
    while counter < 7:
        routes = []
        route = get_random_route(network, connections)
        routes.append(route)
        counter += 1

        if counter == 7:
            Routes(routes)
    pass
    #routes = {}
    #counter = 0


                # voeg de route toe aan de dictionary van routes 
                #routes[counter] = Routes(stations)
                #routes[counter].add_routes(counter, stations) 
                #total_time += time

    # bereken K
    #p = len(connections_used)/len(copy_connections)
    #k = routes[counter].calculate_score(p, counter, total_time)
    #print(k)

    #return routes
