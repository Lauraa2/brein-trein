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
    def __init__(self, startingroutes, stations, total_time, connections):
        self.best_routes = startingroutes   
        self.data_stations = stations
        self.max_time_route = total_time
        self.connections = connections
       
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

    def compare_score(self):
        """
        Checks and accepts better solutions than the current solution.
        Judgement is based on quality score.
        """
        # calculate the score of the old and the new route
        old_score = self.best_routes.calculate_score()
        new_score = self.new_routes.calculate_score()
        
        print(old_score)
        print(new_score) 

        # update the score and route if the new route is better than the old route
        if new_score > old_score:
            self.best_routes = self.new_routes

    def compare_connections(self):
        old_fraction = self.best_routes.calculate_fraction_connections()
        new_fraction = self.new_routes.calculate_fraction_connections()

        print(old_fraction)
        print(new_fraction)

        if new_fraction > old_fraction:
            self.best_routes = self.new_routes

    def run(self, iterations, type):
        """
        Runs the hillclimber algorithm for a specific amount of iterations
        Requires to be told what it has to look at: the score or the fraction of used connections
        """
        if type != 'score' and type != 'connections':
            print('ERROR: for hillclimber choose either \'score\' or \'connections\'')
            exit(1)
        
        for iteration in range(iterations):
            # create a copy of the graph to simulate the change
            self.new_routes = copy.deepcopy(self.best_routes) # Dit self. gemaakt omdat het overal wordt opgeroepen
            
            # change a single route
            self.mutate_single_route()

            # accept it if it is better
            if type == 'score':
                self.compare_score()
            elif type == 'connections':
                self.compare_connections()
                if self.best_routes.check_all_connections():
                    self.best_routes.calculate_score()
                    return self.best_routes
        
        if type == 'connections':
            print('Failed to cover all connections ):')
        
        # return the final route with the highest score
        return self.best_routes
