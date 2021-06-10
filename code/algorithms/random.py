import random
from code.classes.routes import Routes
import copy

def get_random_routes(network):
    """
    Algorithm to gain random routes, with the following constraints:

    1. Max number of routes is 7
    2. Every station is once in the routes
    3. Total time is less than 2 hours

    """
    # laad een lege dictionary om routes in te stoppen
    routes_trajecten = {}
    counter = 0

    # kopieer de stations en stop ze in een lijst zodat we een random object kunnen vinden
    copy_stations = copy.deepcopy(network)
    copy_stations_list = copy.deepcopy(list(copy_stations.items()))

    while len(routes_trajecten) < 7 and len(copy_stations) != 0:

        # maak een lege lijst aan voor stations en routes
        stations = []
        route = []
        
        # pak een random station uit de lijst met stationnetjes
        start_station = random.choice(copy_stations_list) # geeft een random object ('Amsterdam Centraal', <code.classes.station.Station object at 0x7fd015d33310>)
        
        # geeft de naam van het object zelf bijv. 'Amsterdam Centraal'
        start_station_name = start_station[0] 
    
        # voeg de stationsnaam toe aan een route
        route.append(start_station_name)

        # voeg het station toe aan een lijst die de connecties gaat laden 
        stations.append(start_station)

        # set de tijd op 0 voor een nieuw traject
        time = 0

        # zolang de tijd onder twee uur is en er een station beschikbaar is gaan we routes toevoegen
        while time < 120 and start_station[0] in copy_stations:
        
            # verwijder deze vervolgens weer uit de lijst met stationnentjes zodat we geen dubbele stations krijgen
            del copy_stations[start_station[0]] # delete een station uit de lijst met stationnetjes 
            
            # geef aan dat de route nog niet af is en de tijd is nog 0
            connection_end = False

            # laad alle connections van het start station in
            connections_start_station = list(stations[-1][1].connections.items())

            # pak een random connectie uit die lijst en sla ook de tijd op
            for i in range(len(connections_start_station)):
                random_connection = random.choice(connections_start_station)

                # sla de naam op van de connectie
                random_connection_name = random_connection[0]

                # sla de tijd op van de connectie
                time_route = int(random_connection[1])

                # de tijd van de route mag niet over het maximum heen, als dat lukt slaan we de connectie op
                if time + time_route < 120 and random_connection_name in copy_stations: 
                    connection_end = random_connection_name
                    break
                else:
                    # als dat niet kan, verwijderen we de connectie uit de mogelijke connectie lijst
                    connections_start_station.remove(random_connection)

            if connection_end != False:
                # update de totale tijd van de route
                time += time_route

                # voeg de connectie toe aan de route
                route.append(connection_end)

                # maak stations weer leeg zodat een nieuw station geladen kan worden
                stations = []

                # de connectie wordt een nieuw startpunt
                start_station = connection_end

                # maak er een tuple van zodat de rest klopt
                start_station = (connection_end, copy_stations[connection_end])

                # laad dit station in stations
                stations.append(start_station)

            else:
                # als de lengte van de route uit een enkel station bestaat, voegen we er een toe
                if len(route) < 2:
                    connection_end = random_connection_name
                    time += time_route
                    route.append(connection_end)

                # update het aantal routes
                counter += 1

                # voeg de route toe aan de dictionary van routes
                if route not in routes_trajecten:
                    routes_trajecten[counter] = Routes(route)
                    routes_trajecten[counter].add_routes(counter, route)
                    break
                else:
                    break

    return routes_trajecten
