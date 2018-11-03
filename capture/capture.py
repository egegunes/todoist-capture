import sys

import todoist

from capture.secrets import TODOIST_TOKEN


def run():
    api = todoist.TodoistAPI(TODOIST_TOKEN)

    if len(sys.argv) < 2:
        print("Task content is required")
        sys.exit(1)

    api.quick.add(" ".join(sys.argv[1:]))
