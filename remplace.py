import pandas as pd

def replace_stop_names(travel_times_file, stops_file):
    # Charger les fichiers CSV en tant que DataFrames
    travel_times_df = pd.read_csv(travel_times_file)
    stops_df = pd.read_csv(stops_file)

    # Créer un dictionnaire pour mapper les identifiants d'arrêt à leurs noms correspondants
    stop_id_to_name = dict(zip(stops_df['stop_id'], stops_df['stop_name']))

    # Remplacer les identifiants d'arrêt par les noms d'arrêt dans travel_times_df
    travel_times_df['current_stop'] = travel_times_df['current_stop'].map(stop_id_to_name)
    travel_times_df['next_stop'] = travel_times_df['next_stop'].map(stop_id_to_name)

    # Enregistrer le DataFrame modifié dans un nouveau fichier CSV
    travel_times_df.to_csv('travel_times.csv', index=False)

if __name__ == "__main__":
    travel_times_file = 'travel_times.csv'
    stops_file = 'arrets.csv'
    replace_stop_names(travel_times_file, stops_file)
