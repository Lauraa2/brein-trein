from random import random
from code.classes import network, routes, route
from sys import argv
from code.algorithms import random_alg, hillclimber, greedy, simulated_annealing
from code.classes.routes import Routes
from code.visualisations import vision
import matplotlib.pyplot as plt

import statistics
import csv
import math

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
    connections = data.get_connections()
    random_routes = random_alg.get_random_routes(data.stations, connections, time, counter)
    
    print("For a random solution, type 1")
    print("For a Greedy algorithm, type 2")    
    print("For a Hillclimber algorithm based on a random trajectory, type 3")
    print("For a Hillclimber algorithm based on a greedy trajectory, type 4")
    print("For a Simulated Annealing algorithm based on a random trajectory, type 5")
    print("For a Simulated Annealing algorithm based on a greedy trajectory, type 6")
    
    algorithm = input("Select: ")

    if int(algorithm) == 1:

        # print score of random algorithm
        print(random_routes.calculate_score()) 

        # create an output
        random_routes.print_results()

    elif int(algorithm) == 2:

        # print score of greedy algorithm
        greedy_routes = greedy.Greedy(data.stations, time, connections, counter).get_routes()
        print(greedy_routes.calculate_score())

        # create an output
        greedy_routes.print_results()
    
    elif int(algorithm) == 3:
        
        # load climber
        climber = hillclimber.HillClimber(random_routes, data.stations, time, connections)

        # ask for the aim of the hillclimber
        print("For a HillClimber focused on score, type 1")
        print("For a HillClimber focused on connections, type 2")
        focus = input("Select: ") 

        # run the hillcimber
        if int(focus) == 1:
            climber_routes = climber.run(1000, 'score')
        elif int(focus) == 2:
            climber_routes = climber.run(1000, 'connections')

        # print the result
        print(f'max: {climber_routes.score}')

        # create an ouput
        climber_routes.print_results()

    elif int(algorithm) == 4:

        # load climber
        greedy_routes = greedy.Greedy(data.stations, time, connections, counter)
        climber = hillclimber.HillClimber(greedy_routes, data.stations, time, connections)

        # ask for the aim of the hillclimber
        print("For a HillClimber focused on score, type 1")
        print("For a HillClimber focused on connections, type 2")
        focus = input("Select: ") 

        # run the hillclimber
        if int(focus) == 1:
            climber_routes = climber.run(1000, 'score')
        elif int(focus) == 2:
            climber_routes = climber.run(1000, 'connections')
        
        # print the result
        print(f'max: {climber_routes.score}')

        # create an output
        climber_routes.print_results()

    elif int(algorithm) == 5:

        # run simulated annealing
        random_routes = random_alg.get_random_routes(data.stations, connections, time, counter)
        SA = simulated_annealing.Simulated_annealing(random_routes, data.stations, time, connections)
        solution = SA.run(1000)

        # print a score
        print(solution.score)

        # create an output
        solution.print_results()
    
    elif int(algorithm) == 6:
        # run simulated annealing based on greedy
        greedy_routes = greedy.Greedy(data.stations, time, connections, counter)
        SA = simulated_annealing.Simulated_annealing(greedy_routes, data.stations, time, connections)
        solution = SA.run(1000)
        
        # print the score
        print(solution.score)

        # create an output
        solution.print_results()

    vision.draw_solution(f'output.csv', data)
    
    
