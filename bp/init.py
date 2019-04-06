from sys import stderr
from requests import get
from tempfile import gettempdir
from zipfile import ZipFile
from os import path


DATA_DIR = path.realpath(path.dirname(__file__) + '/../data')
ZIP_FILE_URL = 'https://bkk.hu/gtfs/budapest_gtfs.zip'
DOWNLOAD_CHUNK_SIZE = 8192


def download_file(url):
    filename = gettempdir() + '/' + url.split('/')[-1]
    print('Dowloading data...', file=stderr)
    with get(url, stream=True) as req:
        req.raise_for_status()
        with open(filename, 'wb') as file:
            for chunk in req.iter_content(chunk_size=DOWNLOAD_CHUNK_SIZE):
                if chunk:
                    file.write(chunk)
    return filename


def extract_zip(zip_file_path, target_dir):
    print('Extracting data...', file=stderr)
    zipfile = ZipFile(zip_file_path, 'r')
    zipfile.extractall(target_dir)
    zipfile.close()


def init():
    zip_file_path = download_file(ZIP_FILE_URL)
    extract_zip(zip_file_path, DATA_DIR)
