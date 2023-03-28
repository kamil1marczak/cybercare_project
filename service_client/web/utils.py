import json
from pathlib import Path
import os
from loguru import logger

filename = os.environ.get('OUTPUT_FILE_NAME', 'output.json')
file_dir = os.environ.get('OUTPUT_FILE_DIR', 'file_storage')
def get_data_full_path():
    os.environ.get('OUTPUT_FILE_NAME', 'output.json')

    base_path = Path(__file__).resolve().parent.parent
    path_to_data = os.path.join(
        base_path,
        f"{file_dir}",
        f"{filename}"
    )
    logger.debug(f"full data path: {path_to_data}")
    return path_to_data

# function to add to JSON
def write_output_to_json(new_data: json):
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
