import copy
import random

class HillClimber:
    """
    The HillClimber class changes a random route in the network to a random valid route. Each improvement or
    equivalent solution is kept for the next iteration.
    """
    def __init__(self, random_start):

        self.hc_start = copy.deepcopy(random_start)

        #self.score = random_start.get_score()

    def change_single_route(self):
        """
        Change a single route with another random route
        """
        # eerst een random key pakken 
        for key in random.sample(self.hc_start.keys(), 1):

            # dan die random key verwijderen
            del self.hc_start[key]
        
        # dan een nieuwe route toevoegen

        pass

    def change_total_routes(self, new_routes):
        pass

    def compare_score(self, new_routes):
        """
        Checks and accepts better solutions than the current solution.
        """
        new_score = new_routes.get_score()
        old_score = self.score

        if new_score > old_score:
            self.score = new_score
            self.hc_start = new_routes

    def run(self, iterations):
        pass

