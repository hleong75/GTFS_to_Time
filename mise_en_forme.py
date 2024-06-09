import csv

def lire_arrets(nom_fichier):
    arrets = {}
    with open(nom_fichier, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            arrets[row['stop_id'].zfill(4)] = row['stop_name']
    return arrets

def lire_temps_de_trajet(nom_fichier):
    temps_de_trajet = {}
    with open(nom_fichier, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            current_stop = int(row['current_stop'])
            next_stop = int(row['next_stop'])
            time = float(row['travel_time'])
            if current_stop not in temps_de_trajet:
                temps_de_trajet[current_stop] = {}
            temps_de_trajet[current_stop][next_stop] = time
    return temps_de_trajet

def sauvegarder_donnees(arrets, temps_de_trajet, nom_fichier):
    with open(nom_fichier, 'w', encoding='utf-8') as file:
        file.write("[Vertices]\n")
        for stop_id, stop_name in arrets.items():
            file.write(f"{stop_id} {stop_name}\n")

        file.write("[Edges]\n")
        for current_stop, destinations in temps_de_trajet.items():
            for next_stop, time in destinations.items():
                file.write(f"{current_stop} {next_stop} {time}\n")

def main():
    arrets = lire_arrets('arrets.csv')
    temps_de_trajet = lire_temps_de_trajet('travel_time_updated.csv')
    sauvegarder_donnees(arrets, temps_de_trajet, 'data.txt')
    print("Données sauvegardées dans data.txt")

if __name__ == "__main__":
    main()
