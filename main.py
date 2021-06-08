from code.classes import network, routes
from code.algorithms import random
from code.classes.routes import Routes
from code.visualisations import vision
import matplotlib.pyplot as plt

if __name__ == "__main__":

    #x = stations.coordinates

    # Create a graph from our data
    #stations = stations.Station()
    test = network.Network()
    test.print_csv()
    #test.get_random_station()

    test2 = random.get_random_routes(test.stations)
    test3 = routes.print_results(test2)
    #print = routes.Routes.print_results(test2)

    #test1 = routes.Routes.get_random_routes(test.stations)
    #test1.print_results()

    #print = Routes.print_results(test.stations)

    vision = vision.print_stations(test.stations)
    #vision.print_stations()

    #scheme = location.get_location(1)

    # Create visualisation from our data
 

