import argparse
import os

import requests

from shared import BEARER_FILENAME

parser = argparse.ArgumentParser(
    description="Downloads attendance data from Partiful and prints in CSV format. Use > to pipe the output of this program to a file.",
)

parser.add_argument(
    "event_id",
    type=str,
    nargs=1,
    help=(
        "The event id. To find it, navigate to the event page in Partiful and look at the URL in the browser. "
        "The event id is the string of letters and numbers after partiful.com/e/"
    ),
)

namespace = parser.parse_args()

if not os.path.exists(BEARER_FILENAME):
    raise RuntimeError("Credentials file does not exist. Run set_bearer.py first.")

with open(BEARER_FILENAME, "r") as fh:
    bearer_token = fh.read().strip()

res = requests.get(
    f'https://api.partiful.com/getGuestsCsv?eventId={namespace.event_id[0]}&statuses=GOING&statuses=invited&statuses=DECLINED&statuses=MAYBE&questionnaire=true',
    headers={
        'authorization': f'Bearer {bearer_token}',
    },
)

print(res.content.decode('utf-8'))

