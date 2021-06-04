class Node():
    def __init__(self, station):
        self.station = station
        self.connections = {}
        

    def add_connection(self, station, connection, distance):
        self.connections[station] = (connection, distance)
        print(self.connections)


    
       


        
        
