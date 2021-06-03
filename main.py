from code.classes import stations, routes

if __name__ == "__main__":

    # Create a graph from our data
    test = stations.Station("data/StationsHolland.csv")

    location = routes.Location("data/StationsHolland.csv")
    #scheme = location.get_location(1)

