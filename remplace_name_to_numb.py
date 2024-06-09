import pandas as pd

def replace_stop_id_with_numbers(filename):
    # Charge le fichier CSV dans un DataFrame pandas
    df = pd.read_csv(filename)

    # Remplace les valeurs dans la colonne 'stop_id' par des numéros de ligne
    df['stop_id'] = df.index

    # Écrit le DataFrame modifié dans le fichier CSV
    df.to_csv(filename, index=False)

# Remplacez 'arrets.csv' par le nom de votre fichier
if __name__ == "__main__":
    replace_stop_id_with_numbers('arrets.csv')
