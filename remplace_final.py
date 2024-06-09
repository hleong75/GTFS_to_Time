import pandas as pd

def main():
    # Charger les données des fichiers CSV
    travel_time_df = pd.read_csv('travel_times_with_names.csv')
    arrets_df = pd.read_csv('arrets.csv')

    # Créer un dictionnaire pour mapper les noms d'arrêts aux ID d'arrêts
    arrets_mapping = dict(zip(arrets_df['stop_name'], arrets_df['stop_id']))

    # Remplacer les noms d'arrêts par les ID d'arrêts dans travel_time_df
    travel_time_df['current_stop'] = travel_time_df['current_stop'].map(arrets_mapping)
    travel_time_df['next_stop'] = travel_time_df['next_stop'].map(arrets_mapping)

    # Sauvegarder le résultat dans un nouveau fichier CSV
    travel_time_df.to_csv('travel_time_updated.csv', index=False)

    print("Les colonnes current_stop et next_stop ont été mises à jour avec les IDs d'arrêts correspondants.")

if __name__ == "__main__":
    main()
