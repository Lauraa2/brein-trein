"""
# -------------------------------------------------------------------------------
# route.py
# -------------------------------------------------------------------------------
#
# make route objects
#
# Team de Brein Trein
#
"""

class Route():
    def __init__(self):
        '''
        Objects of a route
        '''
        self.stations = []
        self.duration = 0

    def add_station(self, station):
        '''
        Add station to routes
        '''
        self.stations.append(station)

    def current_time(self):
        '''
        Return current time
        '''
        return self.duration

    def last_station(self):
        '''
        Return last station
        '''
        return self.stations[-1]

    def check_station(self, given_station):
        '''
        Check if station is already present in route
        '''
        for station in self.stations:
            if station == given_station:
                return True
        return False

    def update_time(self, time):
        '''
        Update time of route
        '''
        self.duration += time

    def remove_last_station(self):
        '''
        Remove last station if duration of route is to long
        '''
        self.stations.pop()
    