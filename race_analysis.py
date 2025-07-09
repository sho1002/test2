import csv
from statistics import mean
import argparse


def parse_csv(filepath):
    """Load race data from a CSV file."""
    with open(filepath, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)


def average_time_by_driver(rows):
    """Return average lap time for each driver."""
    times_by_driver = {}
    for row in rows:
        driver = row['Driver']
        time = float(row['Time'])
        times_by_driver.setdefault(driver, []).append(time)
    return {driver: mean(times) for driver, times in times_by_driver.items()}


def fastest_lap_by_race(rows):
    """Return the fastest lap in each race."""
    fastest = {}
    for row in rows:
        race = row['Race']
        time = float(row['Time'])
        current = fastest.get(race)
        if current is None or time < current['Time']:
            fastest[race] = {
                'Driver': row['Driver'],
                'Time': time,
                'LapNumber': row['LapNumber'],
            }
    return fastest


def main():
    parser = argparse.ArgumentParser(description='Race data analysis tool')
    parser.add_argument('csvfile', help='CSV file containing race data')
    args = parser.parse_args()

    data = parse_csv(args.csvfile)

    avg_times = average_time_by_driver(data)
    print('Average lap time by driver:')
    for driver, t in avg_times.items():
        print(f'{driver}: {t:.2f} sec')

    fastest = fastest_lap_by_race(data)
    print('\nFastest lap by race:')
    for race, info in fastest.items():
        print(f"{race}: Driver {info['Driver']} Lap {info['LapNumber']} - {info['Time']} sec")


if __name__ == '__main__':
    main()
