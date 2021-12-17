import requests
import os
import zipfile

DATASET_URL = "https://download.microsoft.com/download/3/E/1/3E1C3F21-ECDB-4869-8368-6DEBA77B919F/kagglecatsanddogs_3367a.zip"
DATASET_NAME = 'dataset.zip'

def extract_file(file):
    unzipped_folder = os.path.splitext(file)[0]+''

    if os.path.exists(unzipped_folder):
        return

    with zipfile.ZipFile(file, 'r') as zip_ref:
        zip_ref.extractall(unzipped_folder)

def fetch_dataset(dir=None):
    file_loc = './'

    if not os.path.exists(DATASET_NAME):
        if dir != None:
            file_loc = dir
        
        print('Downloading dataset...')
        dataset_data = requests.get(DATASET_URL)

        open(file_loc + DATASET_NAME, 'wb').write(dataset_data.content)

    extract_file(DATASET_NAME)
