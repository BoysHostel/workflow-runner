import json
from . import Constants


def json_reader(file_name):
    with open(file_name, Constants.READ) as json_file:
        data = json.load(json_file)
    return data


def json_printer(data):
    print(json.dumps(data, indent=4))
