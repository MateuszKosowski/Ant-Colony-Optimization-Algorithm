import json
import glob
import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs("plots", exist_ok=True)

best_solutions = {}

for json_file in glob.glob("results/*.json"):
    with open(json_file) as f:
        data = json.load(f)
        file_name = data["params"]["file"]
        if file_name not in best_solutions or data["path_length"] < best_solutions[file_name]["path_length"]:
            best_solutions[file_name] = data

for file_name, solution in best_solutions.items():
    
    graph_df = pd.read_csv(file_name, sep="\s+", names=["ID", "X", "Y"])
    
    best_path = solution["path"]
    coords = graph_df.set_index("ID").loc[best_path]
    
    plt.figure(figsize=(8,6))
    
    plt.plot(coords["X"], coords["Y"], '-o', color='blue', markersize=8)

    plt.scatter(coords.iloc[0]["X"], coords.iloc[0]["Y"], color='green', s=100, label="Start", zorder=5)
    plt.scatter(coords.iloc[-1]["X"], coords.iloc[-1]["Y"], color='red', s=100, label="Koniec", zorder=5)
    

    for i, row in coords.iterrows():
        plt.text(row["X"]+1, row["Y"]+1, str(i), fontsize=9)
    
    plt.title(f"Nalepsza droga dla {file_name} (Długość: {solution['path_length']:.2f})")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.legend()
    
    safe_name = file_name.replace(".", "_")
    plt.savefig(os.path.join("plots", f"{safe_name}_best_path.png"))
    plt.close()
