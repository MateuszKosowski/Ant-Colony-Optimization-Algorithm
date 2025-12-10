import math
import random


class Ant:

    pheromone_matrix = []

    # classmetod to dekorator, tworzący metodę "statyczną". Działa na zmiennych klasowych a nie obiektach
    @classmethod
    def init_pheromone(cls, places):
        n = len(places.places_list)
        pheromone_matrix = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(1.0)
            pheromone_matrix.append(row)
        Ant.pheromone_matrix = pheromone_matrix

    @classmethod
    def update_pheromone(cls, ants, evaporation_rate=0.5):
        n = len(cls.pheromone_matrix)

        # Parowanie feromonów
        for i in range(n):
            for j in range(n):
                cls.pheromone_matrix[i][j] *= (1 - evaporation_rate)

        # Dodawanie nowych feromonów
        for ant in ants:
            total_distance = sum(ant.distance_travelled)

            pheromone_deposit = 1 / total_distance

            # Aktualizacja dla każdej krawędzi w trasie mrówki
            visited_list = list(ant.visited_places)
            for i in range(len(visited_list) - 1):
                from_place = visited_list[i]
                to_place = visited_list[i + 1]
                cls.pheromone_matrix[from_place.number][to_place.number] += pheromone_deposit
                cls.pheromone_matrix[to_place.number][from_place.number] += pheromone_deposit

    def __init__(self, place, alpha=1.0, beta=1.0, p_random=0.01):
        self.current_place = place
        self.visited_places = []
        self.distance_travelled = list()
        self.alpha = alpha
        self.beta = beta
        self.p_random = p_random

        self.visited_places.append(place)
        self.distance_travelled.append(0)


    def calculate_distance(self, place):
        return math.hypot(
            place.position[0] - self.current_place.position[0],
            place.position[1] - self.current_place.position[1]
        )

    def visit(self, place):
        if place not in self.visited_places:
            self.visited_places.append(place)
        distance = self.calculate_distance(place)
        self.distance_travelled.append(distance)
        self.current_place = place

    def available_places(self, places):
        available_places = []
        for place in places.places_list:
            if place not in self.visited_places and place != self.current_place:
                available_places.append(place)
        return available_places

    def select_next_place(self, places):
        available_places = self.available_places(places)

        if len(available_places) == 0:
            return None


        # Szansa, że mrówka oleje wszystkie zasady i zrobi coś losowo
        if random.random() < self.p_random:
            next_place = random.choice(available_places)
        else:
            numerators = []

            for place in available_places:
                distance = self.calculate_distance(place)
                # Dodajemy małą wartość epsilon, aby uniknąć dzielenia przez zero
                reverse_distance = 1 / (distance + 1e-10)
                pheromone_on_path = Ant.pheromone_matrix[self.current_place.number][place.number]
                numerator = pow(pheromone_on_path, self.alpha) * pow(reverse_distance, self.beta)
                numerators.append(numerator)


            # Metoda ruletki - k to parametr jak dużo obiektów zwrócić, więc bierzemy [0], bo chcemy tylko 1
            # Dodatkowo metoda ta sama znormalizuje dane (czyli to z tym total i dzielenie każdego numerator)
            next_place = random.choices(available_places, weights=numerators, k=1)[0]

        return next_place

    def do_move(self, places):
        next_place = self.select_next_place(places)
        self.visit(next_place)











