import matplotlib.pyplot as plt
import numpy as np

import csv

data = []
trajecten = []
dictionary = {}
trein = {}

def draw_solution(solution_csv, network): # The routes is needed to get all coordinates / station objects
    """
    Map out all routes from a specific solution
    Takes as input the solution as csv file and the network of the problem
    """

    # Different colors to plot each trajectory in
    colors = ['green', 'red', 'blue', 'lime', 'orange', 'cyan', 'yellow', 'magenta', 'black', 'blueviolet' \
        'silver', 'gold', 'silver', 'olivedrab', 'peru', 'violet', 'teal', 'purple', 'royalblue', 'pink']

    file = open(solution_csv)
    reader = csv.DictReader(file)
    
    plt.figure(figsize=(10,10))

    # Initialize counter
    c = 0

    for row in reader:
        # End when the footer of the file is reached
        if row.get('train') == 'score':
            # Save the quality score to later display in the title of the figure                 
            score = row.get('stations')
            break 

        # Retrieve all stations in the trajectory
        stations = row.get('stations')
        
        # Clean up the list of stations
        print(stations)
        stations = stations.strip('[]').split(', ')

        # Get coordinates for each train in the trajectory
        x_values = []
        y_values = []

        for station_name in stations:
            # Acquire the station object
            station = network.stations[station_name]

            # Save the coordinates
            x_values.append(station.x)
            y_values.append(station.y)
            
            # Add the name of the station to the point in the plot
            plt.annotate(station.name, (station.x, station.y))                 

        plt.plot(x_values, y_values, marker='o', color=colors[c], label=f'train {c+1}')
        plt.axis("off")

        # Update counter
        c = c + 1

    # Plot the figure
    
    plt.legend()
    plt.title(f'score = {score}')

    filename = get_file_name(score, '.png')
    plt.savefig(f'solutions/images/{filename}')

def get_file_name(quality, type):
            filename = 'solution_' + str(quality) + type
            return filename
