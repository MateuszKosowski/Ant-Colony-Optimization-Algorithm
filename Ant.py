import math
from random import random


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

    def __init__(self, place, alpha=1.0, beta=1.0):
        self.current_place = place
        self.visited_places = set()
        self.distance_travelled = list()
        self.alpha = alpha
        self.beta = beta

        self.visited_places.add(place)
        self.distance_travelled.append(0)


    def calculate_distance(self, place):
        return math.hypot(
            place.position[0] - self.current_place.position[0],
            place.position[1] - self.current_place.position[1]
        )

    def visit(self, place):
        if place not in self.visited_places:
            self.visited_places.add(place)
        distance = self.calculate_distance(place)
        self.distance_travelled.append(distance)
        self.current_place = place

    def available_places(self, places):
        available_places = []
        for place in places.places_list:
            if place not in self.visited_places:
                available_places.append(place)
        return available_places

    def select_next_place(self, places):
        available_places = self.available_places(places)

        numerators = []

        for place in available_places:
            reverse_distance = 1 / self.calculate_distance(place)
            pheromone_on_path = Ant.pheromone_matrix[self.current_place.number][place.number]
            numerator = pow(pheromone_on_path, self.alpha) * pow(reverse_distance, self.beta)
            numerators.append(numerator)


        # Metoda ruletki - k to parametr jak dużo obiektów zwrócić, więc bieżemy [0]
        # Dodatkowo metoda ta sama zliczy total i podzieli
        next_place = random.choices(available_places, weights=numerators, k=1)[0]

        self.visit(next_place)







