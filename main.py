import pandas as pd
import os
import remplace
import remplace_times
import remplace_name_to_numb
import remplace_final
import mise_en_forme
import doublons
import add_transfers
import stops
import temps
import voisins

def main():
    voisins.main()
    temps.main()
    stops.extract_stop_data('', 'arrets.csv')
    transfers_file = "transfers.txt"
    travel_times_file = "travel_times.csv"
    transfers = add_transfers.load_transfers(transfers_file)
    original_lines, final_lines, lines_equal = add_transfers.update_travel_times(travel_times_file, transfers)
    print("Nombre de lignes dans travel_times.csv avant la modification:", original_lines)
    print("Nombre de lignes dans travel_times.csv après la modification:", final_lines)
    print("Les nombres de lignes sont égaux après la modification:", lines_equal)
    lines_equal = add_transfers.compare_lines(travel_times_file, transfers_file)
    print("Les nombres de lignes entre travel_times.csv et transfers.txt sont égaux:", lines_equal)
    doublons.main()
    stops_file = 'arrets.csv'
    remplace_times.replace_stop_names(travel_times_file, stops_file)
    remplace.replace_stop_names(travel_times_file, stops_file)
    remplace_name_to_numb.replace_stop_id_with_numbers('arrets.csv')
    remplace_final.main()

    mise_en_forme.main()



if __name__=="__main__":
    main()
