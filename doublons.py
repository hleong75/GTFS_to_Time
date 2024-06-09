import csv
import os

def check_duplicate(stop_name, stops):
    for stop in stops:
        if stop['stop_name'] == stop_name:
            return True
    return False

def add_suffix(stop_name, stops):
    i = 1
    new_stop_name = stop_name
    while check_duplicate(new_stop_name, stops):
        new_stop_name = f"{stop_name} {i}"
        i += 1
    return new_stop_name

def main():
    filename = "arrets.csv"
    new_filename = "arrets.csv"
    stops = []

    # Read existing stops
    with open(filename, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            stops.append(row)

    # Update stop names
    for stop in stops:
        stop['stop_name'] = add_suffix(stop['stop_name'], stops)

    # Write updated stops to new file
    with open(new_filename, 'w', newline='') as csvfile:
        fieldnames = ['stop_id', 'stop_name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for stop in stops:
            writer.writerow(stop)

    print("New file created:", new_filename)

if __name__ == "__main__":
    main()
