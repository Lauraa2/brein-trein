from code.classes import network, routes, route
from sys import argv
from code.algorithms import random
from code.algorithms import hillclimber
from code.classes.routes import Routes
from code.visualisations import vision
import matplotlib.pyplot as plt

if __name__ == "__main__":

    if len(argv) == 2:
        region = argv[1]
    else:
        print("Usage: python3 main.py 'Holland' OR 'Nationaal'")
        exit(1)

    stationfile = f"data/Stations{region}.csv"
    connectionfile = f"data/Connecties{region}.csv"

    data = network.Network(stationfile, connectionfile)

    if argv[1] == "Nationaal":
        time = 180
        counter = 20
    else:
        time = 120
        counter = 7

   
    # Create a network from our data
    #network = network.Network()
    connections = data.get_connections()

    #route = route.Route(network.stations)

    # Create random routes and print results
    one_route = random.get_random_routes(data.stations, connections, time, counter)
    #new_routes = routes.Routes(one_route)

    """
    retrieve a random solution and draw it
    """
    #routes = random.get_random_routes(network.stations, connections)
    #vision.draw_solution(f'solutions/csv_files/{routes.filename}', network)

    #stations = random.get_random_routes(network.stations, connections)
    #route = route.Route(stations)
    #results = routes.Routes.print_results(random_routes)

    # Create visualisation from our results
    #vision = vision.print_stations(network.stations, random_routes)

    # Run HillClimber
    #climber = hillclimber.HillClimber(random_routes)
