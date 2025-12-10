# WARTOŚCI BAZOWE (Stałe)

BASE_M = 20           # Liczebność mrówek
BASE_P_RANDOM = 0.01  # Prawdopodobieństwo losowe
BASE_ALPHA = 1.0      # Wpływ feromonów
BASE_BETA = 2.0       # Wpływ heurystyki (odległości)
BASE_RHO = 0.5        # Współczynnik wyparowywania
BASE_T = 500          # Liczba iteracji


EXPERIMENTS = [
    # --- GRUPA 1: Zmienna liczba mrówek (m) ---
    {"m": 10,     "p_random": BASE_P_RANDOM, "alpha": BASE_ALPHA, "beta": BASE_BETA, "rho": BASE_RHO, "T": BASE_T},
    {"m": BASE_M, "p_random": BASE_P_RANDOM, "alpha": BASE_ALPHA, "beta": BASE_BETA, "rho": BASE_RHO, "T": BASE_T},
    {"m": 50,     "p_random": BASE_P_RANDOM, "alpha": BASE_ALPHA, "beta": BASE_BETA, "rho": BASE_RHO, "T": BASE_T},
    {"m": 100,    "p_random": BASE_P_RANDOM, "alpha": BASE_ALPHA, "beta": BASE_BETA, "rho": BASE_RHO, "T": BASE_T},

    # --- GRUPA 2: Zmienne p_random ---
    {"m": BASE_M, "p_random": 0.0,           "alpha": BASE_ALPHA, "beta": BASE_BETA, "rho": BASE_RHO, "T": BASE_T},
    {"m": BASE_M, "p_random": BASE_P_RANDOM, "alpha": BASE_ALPHA, "beta": BASE_BETA, "rho": BASE_RHO, "T": BASE_T},
    {"m": BASE_M, "p_random": 0.05,          "alpha": BASE_ALPHA, "beta": BASE_BETA, "rho": BASE_RHO, "T": BASE_T},
    {"m": BASE_M, "p_random": 0.1,           "alpha": BASE_ALPHA, "beta": BASE_BETA, "rho": BASE_RHO, "T": BASE_T},

    # --- GRUPA 3: Zmienna alpha ---
    {"m": BASE_M, "p_random": BASE_P_RANDOM, "alpha": 0.5,        "beta": BASE_BETA, "rho": BASE_RHO, "T": BASE_T},
    {"m": BASE_M, "p_random": BASE_P_RANDOM, "alpha": BASE_ALPHA, "beta": BASE_BETA, "rho": BASE_RHO, "T": BASE_T},
    {"m": BASE_M, "p_random": BASE_P_RANDOM, "alpha": 2.0,        "beta": BASE_BETA, "rho": BASE_RHO, "T": BASE_T},
    {"m": BASE_M, "p_random": BASE_P_RANDOM, "alpha": 5.0,        "beta": BASE_BETA, "rho": BASE_RHO, "T": BASE_T},

    # --- GRUPA 4: Zmienna beta ---
    {"m": BASE_M, "p_random": BASE_P_RANDOM, "alpha": BASE_ALPHA, "beta": 1.0,       "rho": BASE_RHO, "T": BASE_T},
    {"m": BASE_M, "p_random": BASE_P_RANDOM, "alpha": BASE_ALPHA, "beta": BASE_BETA, "rho": BASE_RHO, "T": BASE_T},
    {"m": BASE_M, "p_random": BASE_P_RANDOM, "alpha": BASE_ALPHA, "beta": 5.0,       "rho": BASE_RHO, "T": BASE_T},
    {"m": BASE_M, "p_random": BASE_P_RANDOM, "alpha": BASE_ALPHA, "beta": 10.0,      "rho": BASE_RHO, "T": BASE_T},

    # --- GRUPA 5: Zmienne rho ---
    {"m": BASE_M, "p_random": BASE_P_RANDOM, "alpha": BASE_ALPHA, "beta": BASE_BETA, "rho": 0.1,      "T": BASE_T},
    {"m": BASE_M, "p_random": BASE_P_RANDOM, "alpha": BASE_ALPHA, "beta": BASE_BETA, "rho": 0.3,      "T": BASE_T},
    {"m": BASE_M, "p_random": BASE_P_RANDOM, "alpha": BASE_ALPHA, "beta": BASE_BETA, "rho": BASE_RHO, "T": BASE_T},
    {"m": BASE_M, "p_random": BASE_P_RANDOM, "alpha": BASE_ALPHA, "beta": BASE_BETA, "rho": 0.8,      "T": BASE_T},

    # --- GRUPA 6: Zmienne T (Iteracje) ---
    {"m": BASE_M, "p_random": BASE_P_RANDOM, "alpha": BASE_ALPHA, "beta": BASE_BETA, "rho": BASE_RHO, "T": 100},
    {"m": BASE_M, "p_random": BASE_P_RANDOM, "alpha": BASE_ALPHA, "beta": BASE_BETA, "rho": BASE_RHO, "T": BASE_T},
    {"m": BASE_M, "p_random": BASE_P_RANDOM, "alpha": BASE_ALPHA, "beta": BASE_BETA, "rho": BASE_RHO, "T": 1000}
]