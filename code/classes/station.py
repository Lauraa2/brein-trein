import csv
from os import X_OK

class Station():
    def __init__(self, name, x, y):
        self.name = name
        self.x = x 
        self.y = y
        self.connections = {}

    def __repr__(self):
        return f'obj:{self.name}'
        
    def add_connection(self, connection, distance):
        self.connections[connection] = distance   
       
    def get_connections(self):
        return list(self.connections.items())

        
        
