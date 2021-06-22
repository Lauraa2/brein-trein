"""
# -------------------------------------------------------------------------------
# simulated_annealing.py
# -------------------------------------------------------------------------------
#
# Tries to improve a given routes solution using a hill climber method enriched with simulated annealing
#
# Team de Brein Trein
#
"""

from code.algorithms import random_alg
from code.algorithms import hillclimber 

import copy
import random
import math


class Simulated_annealing:
    """
    The Simulated annealing class changes one random route from a routes solution and
    decided whether this change is accepted based on the temperature of the system.
    """
    def __init__(self, startingroutes, stations, total_time, connections):
        self.best_routes = startingroutes 
        self.current_routes = self.best_routes  
        self.data_stations = stations
        self.max_time_route = total_time
        self.connections = connections
        
        self.start_t = (-1000) / math.log(0.001, 2)
        self.no_change = 0
        self.counter = 0

    def mutate_single_route(self):
        """
        Change out a single route for another random route
        """
        # remove a random route first
        random_route = random.choice(self.new_routes.routes)
        self.new_routes.remove_route(random_route)
        self.new_routes.update_duration(- random_route.duration)

        # render a new random route 
        new_single_route = random_alg.get_random_route(self.data_stations, self.max_time_route)

        # append the new route to the list of routes and update the duration
        self.new_routes.add_route(new_single_route)
        self.new_routes.update_duration(new_single_route.duration)

    def determine_T(self):
        """
        Determine the temperature of the system
        Cools the system down, unless it seems to be stuck on a value
        """
        # heat the system when stuck
        # keep on heating for a given amount of iterations
        if self.no_change >= self.iterations * 0.1 or (self.counter > 0 and self.counter < (self.iterations * 0.001)):
            T = self.start_t * (1.05 ** self.iteration)
            self.counter += 1
        # cool the system when not stuck
        else:   
            T = self.start_t * (0.997 ** self.iteration)
            self.counter = 0        
        return T   

    def make_decision(self):
        """
        Checks and accepts better solutions than the current solution
        Judgement is based on simulated annealing
        """
        old_score = self.current_routes.calculate_score()
        new_score = self.new_routes.calculate_score()
        
        T = self.determine_T()

        P = 2 ** ((new_score - old_score) / T)
        
        random_value = random.uniform(0, 1)

        if random_value <= P:
            self.current_routes = self.new_routes
            self.no_change = 0

            if self.best_routes.score < self.current_routes.score:
                self.best_routes = self.current_routes

        else: 
            self.no_change += 1

    def run(self, iterations):
        """
        Runs the hillclimber algorithm for a specific amount of iterations
        Uses simulated annealing to prevent getting stuck in a local minimum
        """
        self.iterations = iterations
        for iteration in range(iterations):
            self.iteration = iteration
            # create a copy of the graph to simulate the change
            self.new_routes = copy.deepcopy(self.current_routes) 
            
            # change a single route
            self.mutate_single_route()

            # accept it if it is better
            self.make_decision()
        
        # return the final route with the highest score
        return self.best_routes
