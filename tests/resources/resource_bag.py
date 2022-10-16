import os
from tests.resources import RESOURCES_DIR


def read_file(file):
    path = os.path.join(RESOURCES_DIR, file)
    with open(path, "r") as f:
        contents = f.read()
    return contents


EXAMPLE_RESPONSE = read_file("example_response.json")

EXAMPLE_ENVELOPED_RESPONSE = read_file("example_enveloped_response.json")
