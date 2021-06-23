"""
# -------------------------------------------------------------------------------
# vision.py
# -------------------------------------------------------------------------------
#
# plot routes
#
# Team de Brein Trein
#
"""

import matplotlib.pyplot as plt

import csv


def draw_solution(solution_csv, network): 
    '''
    Map out all routes from a specific solution
    Takes as input the solution as csv file and the network of the problem
    '''

    # different colors to plot each trajectory in
    colors = ['green', 'red', 'blue', 'lime', 'orange', 'cyan', 'yellow', 'magenta', 'black', 'blueviolet', \
        'silver', 'gold', 'silver', 'olivedrab', 'peru', 'violet', 'teal', 'purple', 'royalblue', 'pink']

    file = open(solution_csv)
    reader = csv.DictReader(file)
    
    plt.figure(figsize=(13, 13))

    # initialize counter
    c = 0

    for row in reader:
        # end when the footer of the file is reached
        if row.get('train') == 'score':
            # save the quality score to later display in the title of the figure                 
            score = row.get('stations')
            break 

        # retrieve all stations in the trajectory
        stations = row.get('stations')
        
        # clean up the list of stations
        stations = stations.strip('[]').split(', ')

        # get coordinates for each train in the trajectory
        x_values = []
        y_values = []

        for station_name in stations:
            # acquire the station object
            station = network.stations[station_name]

            x_values.append(station.y)
            y_values.append(station.x)
            
            # add the name of the station to the point in the plot, but only if not too big
            if network.stationfile == f"data/StationsHolland.csv":
                plt.annotate(station.name, (station.y, station.x))                 

        plt.plot(x_values, y_values, marker='o', color=colors[c], label=f'train {c+1}')

        plt.axis("off")

        # update counter
        c = c + 1

    file.close()
    
    # plot the figure
    plt.legend(loc='upper left')
    plt.title(f'score = {score}')

    plt.savefig(f'plot.png')
