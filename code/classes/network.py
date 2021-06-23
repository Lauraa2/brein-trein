"""
# -------------------------------------------------------------------------------
# network.py
# -------------------------------------------------------------------------------
#
# load stations, load connections and print csv 
#
# Team de Brein Trein
#
"""

import csv
from .station import Station


class Network():
    def __init__(self, stationfile, connectionfile):
        '''
        Network attributes
        '''
        self.stations = self.load_station(stationfile)
        self.stationfile = stationfile
        self.connectionfile = connectionfile
        self.load_connections(connectionfile)
        self.get_connections()        
           
    def load_station(self, stationfile):
        '''
        Load all stations 
        '''
        stations = {}

        with open(stationfile) as in_file:
            reader = csv.DictReader(in_file)

            for row in reader:
                stations[row['station']] = Station(row['station'], float(row['x']), float(row['y']))

        return stations 

    def load_connections(self, connectionfile):
        '''
        Loads all the connections to the stations into the loaded nodes (stations) 
        '''
        with open(connectionfile) as in_file:
            reader = csv.DictReader(in_file)
            
            for row in reader:
                connections = []
                distances = []
                distance = row['distance']
                connection = row['station2']
                station = row['station1']
                connections.append(connection)
                distances.append(distance)

                for connection in connections:
                    self.stations[station].add_connection(connection, distance)
                    self.stations[connection].add_connection(station, distance)

    def get_connections(self):
        '''
        Get connections of station
        '''
        connections = []
        for station in self.stations.values():
            for connection in station.connections:
                connections.append((station.name, connection))
        return connections

   