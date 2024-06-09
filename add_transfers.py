import csv

def load_transfers(filename):
    """
    Charge les données de transferts à partir du fichier.

    Args:
        filename (str): Le nom du fichier contenant les données de transferts.

    Returns:
        dict: Un dictionnaire contenant les données de transferts, avec les clés étant les arrêts de départ et les valeurs étant un dictionnaire de correspondance avec les arrêts de destination et les temps de transfert.
    """
    transfers = {}
    with open(filename, 'r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        for row in reader:
            from_stop = row['from_stop_id']
            to_stop = row['to_stop_id']
            transfer_type = row['transfer_type']
            min_transfer_time = row.get('min_transfer_time', 0)
            if transfer_type == '2' or transfer_type == '3':
                if from_stop not in transfers:
                    transfers[from_stop] = {}
                transfers[from_stop][to_stop] = float(min_transfer_time)
    return transfers

def update_travel_times(travel_times_file, transfers):
    """
    Met à jour les temps de trajet avec les données de transferts.

    Args:
        travel_times_file (str): Le nom du fichier contenant les temps de trajet.
        transfers (dict): Un dictionnaire contenant les données de transferts.

    Returns:
        None
    """
    with open(travel_times_file, 'r', newline='', encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        rows = list(reader)
    
    original_lines = len(rows)
    
    updated_rows = []
    for row in rows:
        updated_rows.append(row)
    
    for from_stop in transfers:
        for to_stop in transfers[from_stop]:
            updated_rows.append([from_stop, to_stop, str(transfers[from_stop][to_stop])])

    with open(travel_times_file, 'w', newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file)
        writer.writerows(updated_rows)
    
    final_lines = len(updated_rows)
    
    return original_lines, final_lines, original_lines == final_lines

def compare_lines(filename1, filename2):
    """
    Compare le nombre de lignes entre deux fichiers CSV.

    Args:
        filename1 (str): Le nom du premier fichier CSV.
        filename2 (str): Le nom du deuxième fichier CSV.

    Returns:
        bool: True si le nombre de lignes des deux fichiers est le même, False sinon.
    """
    with open(filename1, 'r', newline='', encoding='utf-8-sig') as file1:
        reader1 = csv.reader(file1)
        lines1 = len(list(reader1))

    with open(filename2, 'r', newline='', encoding='utf-8-sig') as file2:
        reader2 = csv.reader(file2)
        lines2 = len(list(reader2))

    return lines1 == lines2

if __name__ == "__main__":
    transfers_file = "transfers.txt"
    travel_times_file = "travel_times.csv"
    
    # Charger les données de transferts
    transfers = load_transfers(transfers_file)
    
    # Afficher le nombre de lignes avant la modification
    original_lines, final_lines, lines_equal = update_travel_times(travel_times_file, transfers)
    print("Nombre de lignes dans travel_times.csv avant la modification:", original_lines)
    print("Nombre de lignes dans travel_times.csv après la modification:", final_lines)
    print("Les nombres de lignes sont égaux après la modification:", lines_equal)
    
    # Comparer le nombre de lignes entre travel_times.csv et transfers.txt
    lines_equal = compare_lines(travel_times_file, transfers_file)
    print("Les nombres de lignes entre travel_times.csv et transfers.txt sont égaux:", lines_equal)
