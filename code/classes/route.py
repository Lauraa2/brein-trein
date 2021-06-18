
class Route():
    def __init__(self):
        """self.route = stations
        self.duration = time"""
        self.stations = []
        self.duration = 0

    def add_station(self, station):
        self.stations.append(station)

    def current_time(self):
        return self.duration

    def last_station(self):
        return self.stations[-1]

    def check_station(self, given_station):
        """
        Returns True if as station is already present in the route, else False
        """
        for station in self.stations:
            print(" ")
            print(station)
            print(given_station)
            print(" ")
            if station == given_station:
                return True
        return False

    def update_time(self, time):
        self.duration += time

    def remove_last_station(self):
        self.stations.pop()
    