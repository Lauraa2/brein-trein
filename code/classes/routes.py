import csv

from collections import defaultdict



class Location():
    def __init__(self, source_file):
        self.location = self.load_location(source_file)
        
    def load_location(self, source_file):
        """
        Load all the nodes into the graph.
        """
        location = defaultdict(list)

        with open(source_file, 'r') as in_file:
            reader = csv.DictReader(in_file)

            rows = list(reader)

            for row in enumerate(rows):
                x = eval(row['x'])
                y = eval(row['y'])
                for x, y, index in row:
                    location[index].append(coordinates(row['station'], x, y))

        print(location)


def get_location(self, index):
        """
        Returns the transmitters of a specific location.
        """
        if index in self.location:
            return self.location[index]

        raise KeyError("Location does not exist.")



class coordinates():
    """
    Dataclass containing transmitter info.
    """
    def __init__(self, station):
        self.station = station