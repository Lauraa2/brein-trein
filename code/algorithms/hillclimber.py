import copy
import random
from code.classes import network, routes, route
from code.classes.routes import Routes
from code.algorithms import random_alg


class HillClimber:
    """
    The HillClimber class changes a random route in the network to a random valid route. Each improvement or
    equivalent solution is kept for the next iteration.
    """
    def __init__(self, startingroutes, stations, time, connections):
        self.hc_startingroutes = startingroutes
        self.data_stations = stations
        self.max_time_route = time
        self.connections = connections
        #print(self.hc_startingroutes.routes[0].route)
        self.score = routes.Routes.calculate_score(self.hc_startingroutes, self.hc_startingroutes.duration, self.connections)

    def mutate_single_route(self, new_routes):
        """
        Change a single route with another random route
        """
        # remove a random route first
        random_route = random.choice(new_routes.routes)
        new_routes.routes.remove(random_route)

        # render a new random route
        new_single_route = random_alg.get_random_route(self.data_stations, self.max_time_route)

        # append the new route to the list of routes
        new_routes.routes.append(new_single_route)


    def compare_score(self, new_routes):
        """
        Checks and accepts better solutions than the current solution.
        """
        # update the duration of the new route
        total_time = 0
        for i in range(len(new_routes.routes)):
            total_time += new_routes.routes[i].duration

        # calculate the score of the new route
        new_score = routes.Routes.calculate_score(new_routes, total_time, self.connections)
        old_score = self.score
        
        print(old_score)
        print(new_score) 

        # update the score and route if the new route is better than the old route
        if new_score > old_score:
            self.score = new_score
            self.hc_startingroutes = new_routes

    def run(self, iterations):
        """
        Runs the hillclimber algorithm for a specific amount of iterations.
        """
        # the amount of iterations the hillclimber will have
        self.iterations = iterations

        for iteration in range(iterations):

            # create a copy of the graph to simulate the change
            new_routes = copy.deepcopy(self.hc_startingroutes)

            # change a single route
            self.mutate_single_route(new_routes)

            # accept it if it is better
            self.compare_score(new_routes)

        # count the duration
        total_time = 0
        for i in range(len(self.hc_startingroutes.routes)):
            total_time += self.hc_startingroutes.routes[i].duration

        # return the final route with the highest score
        final_routes = Routes(self.hc_startingroutes.routes, total_time, self.connections)
        return final_routes