from bp.data import data
from webbrowser import open
from urllib.parse import quote
from sys import stderr


def map_open(stop_names):
    for stop in data():
        if not stop['name'] in stop_names:
            continue
        pos1 = stop['distance'][1][0]
        pos2 = stop['distance'][1][1]
        positions = (
            pos1[0], pos1[1], pos2[0], pos2[1]
        )
        url = 'https://www.mapdevelopers.com/distance_finder.php?polylines='\
            + quote('[[[[% s, % s], [% s, % s]], "#4286f4"]]' % positions)
        print(url, file=stderr)
        open(url)
        # url = 'https://www.google.com/maps/dir/?api=1'\
        #            '&origin=' + str(pos1[0]) + ',' + str(pos1[1]) +\
        #            '&destination=' + str(pos2[0]) + ',' + str(pos2[1]) +\
        #            '&travelmode=transit'
