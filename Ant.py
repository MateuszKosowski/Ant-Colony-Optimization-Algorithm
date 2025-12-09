import math

class Ant:

    def __init__(self, position, alpha=1.0, beta=1.0):
        self.position = position
        self.visited_places = set()
        self.distance_travelled = list()
        self.alpha = alpha
        self.beta = beta

    def calculate_distance(self, place):
        return math.hypot(place.position[0] - self.position[0], place.position[1] - self.position[1])

    def visit(self, place):
        if place not in self.visited_places:
            self.visited_places.add(place)
        distance = self.calculate_distance(place)
        self.distance_travelled.append(distance)
        self.position = place.position

