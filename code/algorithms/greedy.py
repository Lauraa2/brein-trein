import copy
from code.classes.route import Route

class Greedy:
    """
    The Greedy class takes first the station with the fewest connections and connects the stations to the closest connections
    - The goal is to get as many routes as possible with the lowest time possible
    """
    def __init__(self, network, total_time):
        self.stations  = copy.deepcopy(network)
        self.total_time = total_time
        self.smallest_stations = self.get_smallest_stations()
        self.used_stations = []
        self.get_route()
    
    def get_smallest_stations(self):
        """
        Returns a list of all stations with the lowest number of connections.
        i.e. in the beginning it will return all stations with one connection, once those are gone all stations with two connections.
        """
        smallest_stations = []
        used_stations = []

        # Iterate through all possible stations
        for station in list(self.stations.values()):
            # Check if this station is already being used
            if station in used_stations:
                continue
            # Add the station to the list if the list is empty
            elif not smallest_stations:
                smallest_stations.append(station)
            # Replace the list if the current station has less connections than the stations currently in the list
            elif len(station.connections) < len(smallest_stations[0].connections):
                smallest_stations.clear()
                smallest_stations.append(station)
            # If the current station has as many connections as the stations already in the list, add it
            elif len(station.connections) == len(smallest_stations[0].connections):
                smallest_stations.append(station)
        return smallest_stations
    
    def get_start_station(self):
        for station in self.smallest_stations:
            if station not in self.used_stations:
                self.used_stations.append(station)
                return station
    
    def get_route(self):
        route = Route()
        start_station = self.get_start_station()
        route.add_station(start_station)

        while route.current_time() <= self.total_time:
        # Get the connections from the currently last visited station (E)
            current_station = route.last_station()
            possible_connections = current_station.get_connections()

            # Heuristic chooses closest station as the next (E)
            possible_connections.sort(key=lambda a:float(a[1]))
            new_station = possible_connections[0]
            
