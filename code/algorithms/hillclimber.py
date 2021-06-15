import copy
import random
from code.classes import network, routes, route
from code.algorithms import random_alg


class HillClimber:
    """
    The HillClimber class changes a random route in the network to a random valid route. Each improvement or
    equivalent solution is kept for the next iteration.
    """
    def __init__(self, test):
        pass
        self.hc_startingroutes = test
        #print(self.hc_startingroutes.routes[0].route)
        self.score = routes.Routes.calculate_score(self.hc_startingroutes)


    def mutate_single_route(self, new_routes):
        """
        Change a single route with another random route
        """
        # eerst een random traject verwijderen
        random_route = random.choice(new_routes)
        
        # dan die random key verwijderen
        new_routes.remove(random_route)

        # dan een nieuwe route toevoegen
        new_single_route = random_alg.get_random_route(network.Network().stations, network.Network.get_connections)
        new_routes.append(new_single_route)

    # def mutate_routes(self, new_routes):
    #     """
    #     Changes the value of a number of nodes with a random valid value.
    #     """
    #     for _ in range(number_of_changes):
    #         self.mutate_single_routes(new_routes)


    def compare_score(self, new_routes):
        """
        Checks and accepts better solutions than the current solution.
        """
        new_score = routes.Routes.calculate_score(new_routes)
        old_score = self.score
        
        print(old_score)
        print(new_score) 

        if new_score > old_score:
            self.score = new_score
            self.hc_startingroutes = new_routes

    def run(self, iterations):
        """
        Runs the hillclimber algorithm for a specific amount of iterations.
        """
        self.iterations = iterations

        for iteration in range(iterations):
            # # Nice trick to only print if variable is set to True
            # print(f'Iteration {iteration}/{iterations}, current value: {self.value}') if verbose else None

            # Create a copy of the graph to simulate the change
            new_routes = copy.deepcopy(self.hc_startingroutes)

            self.mutate_single_route(new_routes.routes)

            # Accept it if it is better
            self.compare_score(new_routes)