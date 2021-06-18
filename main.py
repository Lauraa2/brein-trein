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

   
    # retrieve the list of all connections
    connections = data.get_connections()

    #greedy_route = greedy.Greedy(data.stations, time)

    # create a random trajectory
    random_trajectory = random_alg.get_random_routes(data.stations, connections, time, counter)

    # ask user for specific algorithm
    print("For a random solution, type 1")
    print("For a HillClimber algorithm, type 2")

    algorithm = input("Select: ")

    # run random algorithm
    if int(algorithm) == 1:
        print(random_trajectory.calculate_score()) 
        random_trajectory.print_results()

    # run Hillclimber algorithm
    if int(algorithm) == 2:
        
        # load climber
        climber = hillclimber.HillClimber(random_trajectory, data.stations, time, connections)

        print("For a Hillclimber focused on score, type 1")
        print("For a Hillclimber focused on connections, type 2")

        focus = input("Select: ") 

        # run hillclimber based on score
        if int(focus) == 1:
            climber_routes = climber.run(1, 'score')

        # run hillclimber based on the used connections
        elif int(focus) == 2:
            climber_routes = climber.run(10, 'connections')

        print(f'max: {climber_routes.score}')
        climber_routes.print_results()

    # draw the solution
    #vision.draw_solution(f'solutions/csv_files/{run_climber.filename}', data)
