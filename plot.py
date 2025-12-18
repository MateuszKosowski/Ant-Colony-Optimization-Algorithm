import os
import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import glob

sns.set_theme(style="whitegrid")
OUTPUT_DIR = "plots"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def load_results(results_dir="results"):
    data = []
    files = glob.glob(os.path.join(results_dir, "*.json"))
    
    print(f"Znaleziono {len(files)} plików z wynikami.")
    
    for file in files:
        with open(file, 'r') as f:
            try:
                res = json.load(f)
                params = res['params']
                
                entry = {
                    "file": params['file'],
                    "ants": params['ants'],
                    "alpha": params['alpha'],
                    "beta": params['beta'],
                    "p_random": params['p_random'],
                    "iterations": params['iterations'],
                    "evaporation_rate": params['evaporation_rate'],
                    "id": params.get('id', 0),
                    "best_path_length": res['path_length'],
                    "execution_time": res['execution_time'],
                    "path_history": res.get('all_best_distance_in_pop', []),
                    "best_path_coords": res.get('path', [])
                }
                data.append(entry)
            except Exception as e:
                print(f"Błąd w pliku {file}: {e}")
    
    return pd.DataFrame(data)

def plot_parameter_impact(df, param_name, x_label, file_suffix):
    plt.figure(figsize=(10, 6))
    
    unique_vals = sorted(df[param_name].unique())
    
    sns.boxplot(x=param_name, y="best_path_length", data=df, palette="Set3")
    
    means = df.groupby(param_name)['best_path_length'].mean()
    plt.plot(range(len(unique_vals)), means.values, marker='o', color='red', label='Średnia')
    
    plt.title(f"Wpływ parametru {x_label} na długość trasy (mniej = lepiej)")
    plt.ylabel("Długość najlepszej trasy")
    plt.xlabel(x_label)
    plt.legend()
    plt.savefig(f"{OUTPUT_DIR}/impact_{file_suffix}.png")
    plt.close()

def plot_convergence(df, param_name, file_suffix):
    plt.figure(figsize=(10, 6))
    
    unique_vals = sorted(df[param_name].unique())
    
    for val in unique_vals:
        subset = df[df[param_name] == val]
        
        histories = list(subset['path_history'])
        if not histories: continue
        
        min_len = min(len(h) for h in histories)
        histories = [h[:min_len] for h in histories]
        
        avg_history = pd.DataFrame(histories).mean(axis=0)
        
        plt.plot(avg_history, label=f"{param_name}={val}")
        
    plt.title(f"Zbieżność algorytmu w zależności od {param_name}")
    plt.xlabel("Iteracja")
    plt.ylabel("Długość najlepszej trasy")
    plt.legend()
    plt.savefig(f"{OUTPUT_DIR}/convergence_{file_suffix}.png")
    plt.close()

def generate_stats_table(df, group_cols):
    stats = df.groupby(group_cols)['best_path_length'].agg(['mean', 'median', 'std', 'min', 'max']).reset_index()
    stats['execution_time_mean'] = df.groupby(group_cols)['execution_time'].mean().values
    return stats

def main():
    df = load_results()
    if df.empty:
        print("Brak danych do analizy.")
        return

    input_files = df['file'].unique()
    
    for input_file in input_files:
        print(f"Analiza dla pliku: {input_file}")
        sub_df = df[df['file'] == input_file]
        
        cols_to_group = ['ants', 'alpha', 'beta', 'p_random', 'evaporation_rate', 'iterations']
        stats_table = generate_stats_table(sub_df, cols_to_group)
        stats_table.to_csv(f"{OUTPUT_DIR}/stats_{input_file}.csv")
        print(f"Zapisano tabelę statystyk do stats_{input_file}.csv")

        BASE_M = 20
        BASE_P = 0.01
        BASE_A = 1.0
        BASE_B = 2.0
        BASE_RHO = 0.5
        BASE_T = 500
        
        mask = (sub_df['p_random'] == BASE_P) & (sub_df['alpha'] == BASE_A) & \
               (sub_df['beta'] == BASE_B) & (sub_df['evaporation_rate'] == BASE_RHO)
        data_ants = sub_df[mask]
        if not data_ants.empty:
            plot_parameter_impact(data_ants, 'ants', "Liczba Mrówek", f"{input_file}_ants")
            plot_convergence(data_ants, 'ants', f"{input_file}_ants")

        mask = (sub_df['ants'] == BASE_M) & (sub_df['p_random'] == BASE_P) & \
               (sub_df['beta'] == BASE_B) & (sub_df['evaporation_rate'] == BASE_RHO)
        data_alpha = sub_df[mask]
        if not data_alpha.empty:
            plot_parameter_impact(data_alpha, 'alpha', "Alpha (Feromony)", f"{input_file}_alpha")
            plot_convergence(data_alpha, 'alpha', f"{input_file}_alpha")

        mask = (sub_df['ants'] == BASE_M) & (sub_df['p_random'] == BASE_P) & \
               (sub_df['alpha'] == BASE_A) & (sub_df['evaporation_rate'] == BASE_RHO)
        data_beta = sub_df[mask]
        if not data_beta.empty:
            plot_parameter_impact(data_beta, 'beta', "Beta (Heurystyka)", f"{input_file}_beta")

        mask = (sub_df['ants'] == BASE_M) & (sub_df['p_random'] == BASE_P) & \
               (sub_df['alpha'] == BASE_A) & (sub_df['beta'] == BASE_B)
        data_rho = sub_df[mask]
        if not data_rho.empty:
            plot_parameter_impact(data_rho, 'evaporation_rate', "Parowanie (Rho)", f"{input_file}_rho")

        mask = (sub_df['ants'] == BASE_M) & (sub_df['alpha'] == BASE_A) & \
            (sub_df['beta'] == BASE_B) & (sub_df['evaporation_rate'] == BASE_RHO)
        data_p_random = sub_df[mask]
        if not data_p_random.empty:
            plot_parameter_impact(data_p_random, 'p_random', "Prawdopodobieństwo losowe (p_random)", f"{input_file}_p_random")
            plot_convergence(data_p_random, 'p_random', f"{input_file}_p_random")

        mask = (sub_df['ants'] == BASE_M) & (sub_df['alpha'] == BASE_A) & \
            (sub_df['beta'] == BASE_B) & (sub_df['evaporation_rate'] == BASE_RHO) & \
            (sub_df['p_random'] == BASE_P)
        data_iterations = sub_df[mask]
        if not data_iterations.empty:
            plot_parameter_impact(data_iterations, 'iterations', "Liczba Iteracji", f"{input_file}_iterations")
            plot_convergence(data_iterations, 'iterations', f"{input_file}_iterations")


if __name__ == "__main__":
    main()