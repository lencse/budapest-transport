from sys import stderr
from os import path
from csv import reader
from geopy import distance


DATA_FILE = path.realpath(path.dirname(__file__) + '/../data/stops.txt')


def parse(data_file):
    print('Processing data...', file=stderr)
    result = {}
    with open(data_file) as csvfile:
        header = True
        for row in reader(csvfile, delimiter=','):
            if header:
                header = False
                continue
            name = row[1]
            lat = float(row[2])
            lon = float(row[3])
            pos = (lat, lon)
            if name in result:
                result[name]['stops'].append(pos)
            else:
                result[name] = {
                    'name': name,
                    'stops': [pos],
                }
    return result


def data():
    result = []
    parsed = parse(DATA_FILE)
    for stop in parsed:
        stops = parsed[stop]['stops']
        if 1 >= len(stops):
            continue
        greatest_distance = -1
        found = (-1, -1)
        for i in range(0, len(stops) - 1):
            for j in range(i + 1, len(stops)):
                dist = distance.distance(stops[i], stops[j]).meters
                if dist > greatest_distance:
                    found = (i, j)
                    greatest_distance = dist
        result.append({
            'name': stop,
            'distance': (
                greatest_distance,
                (stops[found[0]], stops[found[1]])
            )
        })
    result.sort(key=lambda item: item['distance'][0], reverse=True)
    return result
