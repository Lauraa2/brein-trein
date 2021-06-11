from code.classes import network, routes
from code.algorithms import random
from code.classes.routes import Routes
from code.visualisations import vision
import matplotlib.pyplot as plt

if __name__ == "__main__":

    # Create a network from our data
    network = network.Network()
    connections = network.get_connections()

    # Create random routes and print results
    random_routes = random.get_random_routes(network.stations, connections)
    results = routes.Routes.print_results(random_routes)

    # Create visualisation from our results
    vision = vision.print_stations(network.stations, random_routes)
