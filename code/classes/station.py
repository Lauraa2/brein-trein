import csv
from os import X_OK

class Station():
    def __init__(self, name, x, y):
        self.name = name
        self.x = x 
        self.y = y
        self.connections = {}
        
    def add_connection(self, connection, duration):
        self.connections[duration] = connection
        
    def has_connection(self, connection):
        return connection in self.connections

    def get_connection(self, direction):
        return self.connections[direction]

    
    
    
        




    
       


        
        
