from code.classes import network, routes, route
from code.algorithms import random
from code.algorithms import hillclimber
from code.classes.routes import Routes
from code.visualisations import vision
import matplotlib.pyplot as plt

if __name__ == "__main__":

    # Create a network from our data
    network = network.Network()
    connections = network.get_connections()

    #route = route.Route(network.stations)

    # Create random routes and print results
    one_route = random.get_random_routes(network.stations, connections)
    #new_routes = routes.Routes(one_route)



    #stations = random.get_random_routes(network.stations, connections)
    #route = route.Route(stations)
    #results = routes.Routes.print_results(random_routes)

    # Create visualisation from our results
    #vision = vision.print_stations(network.stations, random_routes)

    # Run HillClimber
    #climber = hillclimber.HillClimber(random_routes)
