from random import random
from code.classes import network, routes, route
from sys import argv
from code.algorithms import random_alg
from code.algorithms import hillclimber 
from code.algorithms import greedy
from code.classes.routes import Routes
from code.visualisations import vision
import matplotlib.pyplot as plt

import statistics
import csv

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

    greedy_routes = greedy.Greedy(data.stations, time, connections, counter)
    #greedy_routes.print_results()

    #route = route.Route(network.stations)

    # Create random routes and print results
    #one_route = random_alg.get_random_route(data.stations, time)
    #print(one_route.stations)
    one_routes = random_alg.get_random_routes(data.stations, connections, time, counter)
    #new_routes = routes.Routes(one_route)

    #stations = random.get_random_routes(network.stations, connections)
    #route = route.Route(stations)
    #results = routes.Routes.print_results(random_routes)

    # Create visualisation from our results
    #vision = vision.print_stations(network.stations, random_routes)
    print("For a random solution, type 1")
    print("For a HillClimber algorithm, type 2")

    algorithm = input("Select: ")

    if int(algorithm) == 1:
        print(one_routes.calculate_score()) 
        one_routes.print_results()

    if int(algorithm) == 2:
        
        # load climber
        climber = hillclimber.HillClimber(one_routes, data.stations, time, connections)

        print("For a HillClimber focused on score, type 1")
        print("For a HillClimber focused on connections, type 2")

        focus = input("Select: ") 

        if int(focus) == 1:
            climber_routes = climber.run(1, 'score')

        elif int(focus) == 2:
            climber_routes = climber.run(10, 'connections')

        #print(f'max: {climber_routes.score}')
        climber_routes.print_results()



    # Run HillClimber
    #climber = hillclimber.HillClimber(one_routes, data.stations, time, connections)
    #print(climber.new_routes)
    # climber_routes = climber.run(1000000, 'connections')
    # climber_routes.print_results()

    #vision.draw_solution(f'solutions/csv_files/{run_climber.filename}', data)
