import json
from pathlib import Path
import os
from loguru import logger

INPUT_FILE_NAME = os.environ.get('INPUT_FILE_NAME', 'input.json')
INPUT_FILE_DIR = os.environ.get('INPUT_FILE_DIR', 'file_storage')

def get_data_full_path():
    base_path = Path(__file__).resolve().parent
    path_to_data = os.path.join(
        base_path,
        f"{INPUT_FILE_DIR}",
        f"{INPUT_FILE_NAME}"
    )
    logger.debug(f"full data path: {path_to_data}")
    return path_to_data

def read_input_file(data_full_path: str):
    with open(data_full_path, encoding='utf-8') as json_file:
        return json.load(json_file)

# function to add to JSON
def write_output_to_json(new_data):
    file_path = get_data_full_path()
    with open(file_path,'r+') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data.append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)
        logger.debug(f"file {file_path} was appended with {new_data}")
