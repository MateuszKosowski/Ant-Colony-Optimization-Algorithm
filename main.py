import json
from random import choice
import argparse
import time

from ant import Ant
from places import Places


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", required=True, type=str)
    parser.add_argument("-n", "--ants", required=True, type=int)
    parser.add_argument("-a", "--alpha", required=True, type=float)
    parser.add_argument("-b", "--beta", required=True, type=float)
    parser.add_argument("-p", "--p_random", required=True, type=float)
    parser.add_argument("-i", "--iterations", required=True, type=int)
    parser.add_argument("-e", "--evaporation_rate", required=True, type=float)
    parser.add_argument("-id", "--id", required=True, type=float)
    args = parser.parse_args()

    all_places = Places(args.file)

    Ant.init_pheromone(all_places)

    best_solution = None
    best_distance = float('inf')
    all_worst_distance_in_pop = []
    all_avg_distance_in_pop = []
    all_best_distance_in_pop = list()

    start_time = time.perf_counter()

    for iteration in range(args.iterations):
        ants = []

        worst_distance_in_pop = 0.0
        sum_distance = 0

        for i in range(args.ants):
            random_position = choice(all_places.places_list)
            ant = Ant(random_position, args.alpha, args.beta, args.p_random)
            ants.append(ant)

        for _ in range(len(all_places.places_list) - 1):
            for ant in ants:
                ant.do_move(all_places)

        Ant.update_pheromone(ants, args.evaporation_rate)



        for ant in ants:
            sum_distance += sum(ant.distance_travelled)
            if sum(ant.distance_travelled) < best_distance:
                best_solution = ant.visited_places
                best_distance = sum(ant.distance_travelled)
            if sum(ant.distance_travelled) > worst_distance_in_pop:
                worst_distance_in_pop = sum(ant.distance_travelled)

        avg_distance_in_pop = sum_distance / len(ants)

        all_worst_distance_in_pop.append(worst_distance_in_pop)
        all_avg_distance_in_pop.append(avg_distance_in_pop)
        all_best_distance_in_pop.append(best_distance)

        if iteration % 50 == 0:
            print(f"Iteracja {iteration}: Najlepsza odległość = {best_distance}")

    end_time = time.perf_counter()
    execution_time = end_time - start_time


    print(f"\nNajlepsze rozwiązanie: {best_distance}")
    route_numbers = [place.number + 1 for place in best_solution]
    print(f"Trasa: {route_numbers}")
    print(f"Czas wykonania: {execution_time:.3f} sekund")

    results = {
        "params": {
            "file": args.file,
            "ants": args.ants,
            "alpha": args.alpha,
            "beta": args.beta,
            "p_random": args.p_random,
            "iterations": args.iterations,
            "evaporation_rate": args.evaporation_rate
        },
        "path_length": best_distance,
        "path": route_numbers,
        "all_worst_distance_in_pop": all_worst_distance_in_pop,
        "all_avg_distance_in_pop": all_avg_distance_in_pop,
        "all_best_distance_in_pop": all_best_distance_in_pop,
        "execution_time": execution_time,
    }

    with open(f"results/result_f{args.file}_n{args.ants}_a{args.alpha}_b{args.beta}_p{args.p_random}_i{args.iterations}_e{args.evaporation_rate}_id{args.id}.json", "w") as f:
        json.dump(results, f)

if __name__ == '__main__':
    main()