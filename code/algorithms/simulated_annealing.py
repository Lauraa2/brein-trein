import copy
import random
from code.classes import network, routes, route
from code.classes.routes import Routes
from code.algorithms import hillclimber, random_alg


class Simulated_annealing:
    """
    The HillClimber class changes a random route in the network to a random valid route. Each improvement or
    equivalent solution is kept for the next iteration.
    """
    def __init__(self, startingroutes, stations, total_time, connections):
        self.best_routes = startingroutes   
        self.data_stations = stations
        self.max_time_route = total_time
        self.connections = connections
        self.current_routes = self.best_routes

        self.cutoff = 0.005
       

    def compare_score(self):
        """
        Checks and accepts better solutions than the current solution.
        Judgement is based on quality score.
        """
        # calculate the score of the old and the new route
        old_score = self.current_routes.calculate_score()
        new_score = self.new_routes.calculate_score()
        
        #print(old_score)
        #print(self.best_routes.score) 

        difference = (new_score - old_score) / old_score

        if difference > 0:
            self.current_routes = self.new_routes
        elif difference > - self.cutoff:
            self.current_routes = self.new_routes

        if self.current_routes.score > self.best_routes.score:
            self.best_routes = self.current_routes
            

    def run(self, iterations):
        """
        Runs the hillclimber algorithm for a specific amount of iterations
        Uses simulated annealing to prevent 
        """        
        for iteration in range(iterations):
            # create a copy of the graph to simulate the change
            self.new_routes = copy.deepcopy(self.current_routes) 
            
            # change a single route
            hillclimber.mutate_single_route()

            # accept it if it is better
            self.compare_score()
        
        # return the final route with the highest score
        return self.best_routes
