import csv
from .node import Node



class Station():
    def __init__(self):
        self.stations = self.load_station()
        self.load_connections()
        
        
    def load_station(self):
        """
        Load all the stations
        """
        stations = {}
        coordinates = {}

        with open("data/StationsHolland.csv", 'r') as in_file:
            reader = csv.DictReader(in_file)

            for row in reader:
                stations[row['station']] = Node(row['station'])

                coordinates[row['station']] = [row['x'], row['y']]
                #coordinates[row['station']] = row['y']
                
                #coordinates[row['x']] = Node(row['x'])
                #coordinates[row['y']] = Node(row['y'])
            #print(stations)
        #return stations

        return stations 

    def load_connections(self):
        """
        Loads all the connections to the stations into the loaded nodes (stations) 
        """
        with open("data/ConnectiesHolland.csv", 'r') as in_file:
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
    
    def print_csv(self):
        """
        Method to print the csv file with output
        """
        with open('data.csv', 'w', newline='') as csvfile:
            fieldnames = ['train', 'stations', 'connection']
            thewriter = csv.DictWriter(csvfile, fieldnames = fieldnames)
            thewriter.writeheader()
            trains_count = 0

            for node in self.stations.values():
                trains_count += 1
                thewriter.writerow({'train': trains_count, 'stations': node.station, 'connections': node.connections})
                
           
                
                
                    
            
                

            
            




