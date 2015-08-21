import os

import yaml


def get_config():
    home = os.path.expanduser("~")
    with open(os.path.join(home, ".pystart.yml")) as yaml_data:
        return yaml.load(yaml_data)
