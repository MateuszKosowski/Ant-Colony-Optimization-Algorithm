import subprocess
import os
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import Process

from test_kits import *

def launch(params):
    cmd = [
        'python', 'main.py',
        '-f', str(params['file']),
        '-n', str(params['ants']),
        '-a', str(params['alpha']),
        '-b', str(params['beta']),
        '-p', str(params['p_random']),
        '-i', str(params['iterations']),
        '-e', str(params['evaporation_rate']),
        '--id', str(params['id'])
    ]
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Crash with parameters: {params}")
        print(f"Error: {e}")


def main():

    jobs = []

    for exp in EXPERIMENTS:
        experiment_1 = {
            "file": "A-n32-k5.txt",
            "ants": exp["m"],
            "alpha": exp["alpha"],
            "beta": exp["beta"],
            "p_random": exp["p_random"],
            "iterations": exp["T"],
            "evaporation_rate": exp["rho"]
        }

        experiment_2 = {
            "file": "A-n80-k10.txt",
            "ants": exp["m"],
            "alpha": exp["alpha"],
            "beta": exp["beta"],
            "p_random": exp["p_random"],
            "iterations": exp["T"],
            "evaporation_rate": exp["rho"]
        }

        jobs.append(experiment_1)
        jobs.append(experiment_2)
    all_jobs = []
    for job in jobs:
        for r in range(5):
            new_job = job.copy()
            new_job['id'] = r
            all_jobs.append(new_job)

    print(len(all_jobs))
    with ProcessPoolExecutor(max_workers=os.cpu_count()) as executor:
        executor.map(launch, all_jobs)

if __name__ == '__main__':
    main()
