import math

class Ant:

    pheromone_matrix = []

    # classmetod to dekorator, tworzący metodę "statyczną". Działa na zmiennych klasowych a nie obiektach
    @classmethod
    def init_pheromone(cls, places):
        if cls.pheromone_matrix:
            return

        n = len(places.places_list)
        pheromone_matrix = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(1.0)
            pheromone_matrix.append(row)
        Ant.pheromone_matrix = pheromone_matrix

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

    def available_places(self, places):
        available_places = []
        for place in places.places_list:
            if place.number not in self.visited_places:
                available_places.append(place)
        return available_places

    def select_next_place(self, places):
        available_places = self.available_places(places)

        for place in available_places:
            reverse_distance = 1 / self.calculate_distance(place)



