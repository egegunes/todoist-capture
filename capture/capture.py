import configparser
import os
import sys

import todoist

def run():
    config = configparser.ConfigParser()
    config.read(os.path.join(os.getenv("HOME"), ".todoist"))

    print(config["todoist"]["token"])

    api = todoist.TodoistAPI(config["todoist"]["token"])

    if len(sys.argv) < 2:
        print("Task content is required")
        sys.exit(1)

    api.quick.add(" ".join(sys.argv[1:]))
