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
    #network = network.Network()
    connections = data.get_connections()

    
    for i in range(100):
        one_routes = random_alg.get_random_routes(data.stations, connections, time, counter)
        print(one_routes.calculate_score())

    #greedy_routes = greedy.Greedy(data.stations, time, connections, counter)
    #greedy_routes.print_results()

    #sroute = route.Route(network.stations)

    # Create random routes and print results
    #one_route = random_alg.get_random_route(data.stations, time)
    #print(one_route.stations)
    #one_routes = random_alg.get_random_routes(data.stations, connections, time, counter)
    #new_routes = routes.Routes(one_route)
    
    # with open(f'solutions/analyse/SA.csv') as file:
    #     reader = csv.reader(file)
    #     values = next(reader)
    #     values = next(reader)
    #     values = values[1]
    #     values = values.strip('[]').split(', ')
    #     values = list(map(float, values))

    # times = []
    # for i in range(1000):
    #     times.append(i)


    # plt.plot(times, values, marker='o', color='#5f8195')
    # plt.axis([0, 1000, 4000, 8000])
    # plt.xlabel('aantal trajecten')
    # plt.xticks(times)
    # plt.ylabel('gemiddelde p')
    # plt.savefig('solutions/analyse/SA.png')

    
    # one_routes = random_alg.get_random_routes(data.stations, connections, time, counter)
    # SA = simulated_annealing.Simulated_annealing(one_routes, data.stations, time, connections)
    # solution = SA.run(1000)
    # greedy_routes = greedy.Greedy(data.stations, time, connections, counter)
    # solution = greedy_routes.run()

    # print(solution.score)
    '''
    all_p = []
    all_time = []
    all_score = []
    
    for i in range(100):
        print(i)
        # run simulated annealing
        # one_routes = random_alg.get_random_routes(data.stations, connections, time, counter)
        # greedy_routes = greedy.Greedy(data.stations, time, connections, counter).get_routes()
        # climber = hillclimber.HillClimber(greedy_routes, data.stations, time, connections)
        # SA = simulated_annealing.Simulated_annealing(one_routes, data.stations, time, connections)
        #solution = SA.run(1000)
        # SA = simulated_annealing.Simulated_annealing(one_routes, data.stations, time, connections)
        # solution = SA.run(1000)
        solution = greedy.Greedy(data.stations, time, connections, counter)
        print(solution)
        # print(solution.score)
        p = solution.calculate_fraction_connections()
        print(p)
        all_p.append(p)
        score = solution.calculate_score()
        print(score)
        all_score.append(score)

        all_time.append(solution.duration)
    

    with open(f'solutions/analyse/SA_nationaal/1.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['p', all_p])
        writer.writerow(['score', all_score])
        writer.writerow(['time', all_time])

    
    with open(f'solutions/analyse/SA_nationaal/1.csv') as file:
            reader = csv.reader(file)
            values = next(reader)
            values = next(reader)
            values = values[1]
            values = values.strip('[]').split(', ')
            values = list(map(float, values))
            average = sum(values) / len(values)
            minvalue = min(values)
            maxvalue = max(values)
    
    print(average)
    print(minvalue)
    print(maxvalue)
    '''
    '''
    #stations = random.get_random_routes(network.stations, connections)
    #route = route.Route(stations)
    #results = routes.Routes.print_results(random_routes)
    
    # Create visualisation from our results
    #vision = vision.print_stations(network.stations, random_routes)
    print("For a random solution, type 1")
    print("For a Hillclimber algorithm, type 2")
    print("For a Greedy algorithm, type 3")
    print("For a Simulated Annealing algorithm, typ 4")
    
    algorithm = input("Select: ")
    if int(algorithm) == 1:
        print(one_routes.calculate_score()) 
        one_routes.print_results()
    
    elif int(algorithm) == 2:
        
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

    elif int(algorithm) == 3:
        greedy_routes = greedy.Greedy(data.stations, time, connections, counter)
        greedy_routes.print_results()

    elif int(algorithm) == 4:
        all_p = []
        all_time = []
        all_score = []
        
        for i in range(100):
            print(i)
            # run simulated annealing
            one_routes = random_alg.get_random_routes(data.stations, connections, time, counter)
            SA = simulated_annealing.Simulated_annealing(greedy_routes, data.stations, time, connections)
            solution = SA.run(3)
            print(solution.score)
            p = solution.calculate_fraction_connections()
            all_p.append(p)

        score = solution.calculate_score()
        all_score.append(score)

        all_time.append(solution.duration)
        

        with open(f'solutions/analyse/SA_nationaal/1.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['p', all_p])
            writer.writerow(['score', all_score])
            writer.writerow(['time', all_time])

        
        with open(f'solutions/analyse/SA_nationaal/1.csv') as file:
                reader = csv.reader(file)
                values = next(reader)
                values = next(reader)
                values = values[1]
                values = values.strip('[]').split(', ')
                values = list(map(float, values))
                average = sum(values) / len(values)
        
        print(average)



        
    # Run HillClimber
    #climber = hillclimber.HillClimber(one_routes, data.stations, time, connections)
    #print(climber.new_routes)
    # climber_routes = climber.run(1000000, 'connections')
    # climber_routes.print_results()
    
    vision.draw_solution(f'output.csv', data)
    '''
    
