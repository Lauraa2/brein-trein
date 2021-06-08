from .station import Station
import random
#from .network import Network

class Routes():
    def __init__(self):
        self.routes = self.get_random_routes()
        #self.routes2 = self.get_all_routes(start, destination, du)

    def get_random_routes(test):
        duration = 0
        stations =[]
        networks = list(test.items())
        station = random.choice(networks)
        routes = []
        #print(station)
        #stations.append(station)
        
        for test in networks:
            start_station = test
            i = 0
            route = []
            while True: 
                stations.append(start_station)
                connections = list(stations[-1][1].connections.items())
                print(connections)
                self.get_random_routes(test)

                connection = connections[i][1] 

                if start_station == connection:
                    return [route]

                if i == (len(connections) - 1):
                    return False
                i += 1
            
                route = route + [start_station]

                print(start_station)
                start_station = connection
                stations = []
                return True
                print(start_station)
                return False
                #print(route)

                #print(station)
                
                # for connection in connections:
                    
                #     start_station = connection[1]

                #     print(connection[1])
                #     return False

                    #return False
        # while duration <= 120:
        #next = list(stations[-1][1].connections.items())
        #print(next)
        #     next_random = random.choice(next)

        #     for network in networks:
        #         if next_random[0] == network[0]:
        #             stations.append(network)

            #duration += int(next_random[1])
        #print(networks)
        # print(station)
        # print(stations[-1][1])
        # print(list(stations[-1][1].connections.values())[0])
        # print(stations[-1][1].connections.keys())
        #print(duration)
        #print(stations)

    def get_all_routes(self, start, destination, duration=0):
        routes = routes + start
        networks = list(test.items())
        print(networks)

        for station in networks:


            print(station)


    


