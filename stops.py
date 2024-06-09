import pandas as pd

def extract_stop_data(gtfs_file_path, output_csv_path):
    # Charger les données des arrêts (stops) depuis le fichier GTFS
    stops_df = pd.read_csv(gtfs_file_path + 'stops.txt')

    # Sélectionner les colonnes stop_id et stop_name
    stop_data = stops_df[['stop_id', 'stop_name']]

    # Écrire les données dans un fichier CSV
    stop_data.to_csv(output_csv_path, index=False)

if __name__ == "__main__":
    extract_stop_data('', 'arrets.csv')
