
class Route():
    def __init__(self, stations):
        self.route = self.get_route(stations)
    
    def get_route(self, stations):
        route = []
        route.append(stations)
        return route
