from random import randint

from ant import Ant
from places import Places


def main():

    file_to_load = "A-n32-k5.txt"
    number_of_ants = 50
    ant_alpha = 1.0
    ant_beta = 2.0
    p_random = 0.01
    number_of_iterations = 500
    evaporation_rate = 0.5

    all_places = Places(file_to_load)

    Ant.init_pheromone(all_places)
    best_solution = None
    best_distance = float('inf')

    for iteration in range(number_of_iterations):
        ants = []

        for i in range(number_of_ants):
            random_position = all_places.places_list[randint(0, len(all_places.places_list) - 1)]
            ant = Ant(random_position, ant_alpha, ant_beta, p_random)
            ants.append(ant)

        for _ in range(len(all_places.places_list) - 1):
            for ant in ants:
                ant.do_move(all_places)

        Ant.update_pheromone(ants, evaporation_rate)
        for ant in ants:
            if sum(ant.distance_travelled) < best_distance:
                best_solution = ant.visited_places
                best_distance = sum(ant.distance_travelled)

        if iteration % 50 == 0:
            print(f"Iteracja {iteration}: Najlepsza odległość = {best_distance}")

    print(f"\nNajlepsze rozwiązanie: {best_distance}")

    route_numbers = [place.number + 1 for place in best_solution]
    print(f"Trasa: {route_numbers}")


if __name__ == '__main__':
    main()