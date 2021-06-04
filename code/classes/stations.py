import csv
from .node import Node


class Station():
    def __init__(self, source_file):
        self.stations = self.load_station(source_file)
        
    def load_station(self, source_file):
        """
        Load all the stations
        """
        stations = {}
        with open(source_file, 'r') as in_file:
            reader = csv.DictReader(in_file)

            for row in reader:
<<<<<<< HEAD
<<<<<<< HEAD
                stations[row['station1']] = Node(row['station1'], row['station1'])
                stations[row['station2']] = Node(row['station2'], row['station2'])

        #print(stations)
        return stations

    def load_destination(self, source_file):
        """
        Load all the destinations into the loaded nodes.
        """
        with open(source_file, 'r') as in_file:
            reader = csv.DictReader(in_file)

            for row in reader:
                destinations = []
                destinations.append(row['station2'])

                station_id = row['station1']
                print(station_id)

                # Add the destination to the correct node
                for destination in destinations:
                    destination2 = self.stations[destination]
                    self.stations[station_id].add_destination(destination2)
=======
                stations[row['station1'], row['station2'], row['distance']] = Node(row['station1'], row['station2'], row['distance'])
                #destinations[row['station2']] = Node(row['station1'], row['station2'])
        

        #print(stations)
        for key, value in stations.items():
            print(key[0])
            print(key[1])
            print(key[2])
            print(value)
        #print(destinations)
        
=======
                stations[row['station']] = Node(row['station'])
    
>>>>>>> 05fd63d43c15015eb847d509efb4799377cc762b
        return stations


>>>>>>> 7e32acd85d56d10e61597008c605cc35cd5130f8
