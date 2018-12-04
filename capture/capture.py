try:
    import configparser
except ImportError:
    import ConfigParser as configparser

import os
import sys

import todoist

def run():
    config = configparser.ConfigParser()
    config.read(os.path.join(os.getenv("HOME"), ".todoist"))

    try:
        token = config["todoist"]["token"]
    except AttributeError:
        token = config.get("todoist", "token")

    api = todoist.TodoistAPI(token)

    if len(sys.argv) < 2:
        print("Task content is required")
        sys.exit(1)

    api.quick.add(" ".join(sys.argv[1:]))
