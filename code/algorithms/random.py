import random
from code.classes.routes import Routes
import copy

def get_random_routes(network, connections):
    """
    Algorithm to gain random routes, with the following constraints:
    1. Max number of routes is 7
    2. Every link is only once in the routes
    3. Total time is less than 2 hours
    """
    # laad een lege dictionary om routes in te stoppen
    routes = {}
    counter = 0

    # kopieer de stations en stop ze in een lijst zodat we een random object kunnen vinden
    copy_stations = copy.deepcopy(network)
    copy_stations_list = list(copy_stations.items())
    copy_connections = copy.deepcopy(connections)

    # maak een lijst voor alle bereden verbindingen
    connections_used = []

    #while len(routes) < 1:

        # maak een lege lijst aan voor stations 
    stations = []

    # pak een random station uit de lijst met stationnetjes
    start_station = random.choice(copy_stations_list) # geeft een random object ('Amsterdam Centraal', <code.classes.station.Station object at 0x7fd015d33310>)
    
    # geeft de naam van het object zelf bijv. 'Amsterdam Centraal'
    start_station_name = start_station[0] 

    # voeg het station toe aan een lijst die de connecties gaat laden 
    stations.append(start_station)

    # zet de tijd op 0 voor een nieuw traject
    time = 0

    #while time <= 120:

    connections_start_station = list(stations[-1][1].connections.items())
    print(connections_start_station)
    new_station = stations[-1][0] # is hetzelfde als start_station_name
    print(new_station)
    random_connection = random.choice(connections_start_station)
    print(random_connection)
    random_connection_name = random_connection[0]

    check = True

    #         # check of de gemaakte verbinding al is bereden of niet, zo nee, voeg toe aan verbindingen
    #         for connection in copy_connections:
    #             if connection[0] == new_station and connection[1] == random_connection_name:
    print(connections_used)
    if len(connections_used) > 0:
        for connection_used in connections_used:
            print("ho")
            if connection_used[0] == new_station and connection_used[1] == random_connection_name:
                check = False
                print(check)
 
    #                         continue

    if check != False:
        connections_used.append((new_station, random_connection_name))
        time_route = int(random_connection[1])

    #             # add the station object of the connection to the stations list
        for station in copy_stations_list:
            if station[0] == random_connection_name:
                stations.append(station)
            
    #             # update de totale tijd van de route
        time += time_route
        print(time)
        print(connections_used)
    #             # update het aantal routes
    #             if time >= 120:
    #                 print(connections_used)
    #                 p = len(connections_used)/len(copy_connections)
    #                 print(p)
    #                 counter += 1
    #                 # voeg de route toe aan de dictionary van routes
    #                 routes[counter] = Routes(stations)
    #                 routes[counter].add_routes(counter, stations)
    #                 break
    #         else:
    #             break

    # return routes