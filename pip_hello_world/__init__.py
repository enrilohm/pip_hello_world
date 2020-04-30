from pip_hello_world.pip_hello_world import *

import os

_ROOT = os.path.abspath(os.path.dirname(__file__))


def get_data_path(path):
    return os.path.join(_ROOT, "data", path)


def get_source_path(path):
    return os.path.join(_ROOT, path)
