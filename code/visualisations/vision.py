import matplotlib.pyplot as plt
import numpy as np
from code.classes import network
from code.classes import routes
from code.algorithms import random
import csv

coordinates = []

data = []

trajecten = []

dictionary = {}

#bla = random
#print(bla)

def print_stations(test, test2):

    print("")
    print("")
    print("")
    print("")
    #print(test)
    #print(trajecten)


    for key,value in test2.items():
        print(test2.items())
        print(" ")
        #print("Key : {} , Value : {}".format(key,value.x))
        trajecten.append(value.stations)
        print(trajecten)

    #for key,value in test.items():
        #print("Key : {} , Value : {}".format(key,value.x))
     #   data.append([float(value.x), float(value.y)])


    for key,value in test.items():
        #print("Key : {} , Value : {}".format(key,value.x))
        dictionary[key] = [float(value.x), float(value.y)]
        #data.append([float(value.x), float(value.y)])

    
    #for key,value in dictionary.items():
     #   key = key
      #  x = float(value[0])
       # y = float(value[1])
        #for traject in trajecten:
         #   for station in traject:
          #      if key == station[0]:
           #         print(test)

    for traject in trajecten:
        for station in traject:
            if station[0] in dictionary:
                data.append(dictionary[station[0]])
                print(dictionary[station[0]])

        y, x = zip(*data)
        plt.ylim(51.5, 53)
        plt.xlim(4.2, 5.2)
        plt.plot(x, y, '-ok')
        plt.savefig("plot.png")
        plt.show()
                #break
                #x = value.x
                #y = value.y
                #coordinates.append([x, y])
            #print(station[0])

       
    #z = zip(*trajecten)
    #print(key)
    #print(x)
    #print(y)
    #print(dictionary.items())

    #y, x = zip(*data)
    #plt.ylim(51.5, 53)
    #plt.xlim(4.2, 5.2)
    #plt.plot(x, y, '-ok')
    #plt.savefig("plot.png")
    #plt.show()