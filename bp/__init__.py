from bp.data import DATA_FILE
from os.path import isfile
from bp.init import init


if not isfile(DATA_FILE):
    init()
