"""
# -------------------------------------------------------------------------------
# station.py
# -------------------------------------------------------------------------------
#
# make station objects
#
# Team de Brein Trein
#
"""

class Station():
    def __init__(self, name, x, y):
        '''
        Station attributes
        '''
        self.name = name
        self.x = x 
        self.y = y
        self.connections = {}

    def __repr__(self):
        return f'obj:{self.name}'
        
    def add_connection(self, connection, distance):
        '''
        Add connection between stations  
        '''
        self.connections[connection] = distance   
       
    def get_connections(self):
        '''
        Get the connections
        '''
        return list(self.connections.items())

        
        
