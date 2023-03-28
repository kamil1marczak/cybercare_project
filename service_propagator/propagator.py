# importing the requests library
import json
import requests
import random
import time
from loguru import logger
from service_propagator.utils import get_data_full_path, read_input_file
import os

PERIOD_S = os.environ.get('PERIOD_SECONDS', int(3))
EVENT_ENDPOINT = os.environ.get('EVENT_ENDPOINT', "event")

def propagate_to_api(event):
    # defining the api-endpoint
    API_ENDPOINT = f"http://127.0.0.1:8000/api/{EVENT_ENDPOINT}"

    # sending post request and saving response as response object
    r = requests.post(url=API_ENDPOINT, data=json.dumps(event))
    # extracting response text
    response = r.text
    logger.debug(f"response: {response}")
    # print("The pastebin URL is:%s" % pastebin_url)
    return response

class PropagatorApp():
    data_full_path: str
    event_stack: list
    def __init__(self):

        self.data_full_path = get_data_full_path()
        self.event_stack = read_input_file(self.data_full_path)
        logger.debug(f"loaded file: {self.data_full_path}")
        logger.debug(f"event_stack: {self.event_stack}")

    @property
    def get_number_of_events(self):
        number_of_events = len(self.event_stack)
        logger.debug(f"get_number_of_events: {number_of_events}")
        return number_of_events

    def select_random_event(self):
        index = random.choice(range(self.get_number_of_events))
        selected_event = self.event_stack.pop(index)
        logger.debug(f"selected_event: {selected_event}")
        return selected_event

    def run(self):
        print(" [x] Requesting data from json file")
        while self.get_number_of_events > 0:
            event = self.select_random_event()
            request = propagate_to_api(event)
            print(" [.] Got %r" % request)
            time.sleep(int(PERIOD_S))
