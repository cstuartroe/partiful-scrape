import json

import requests

from shared import BEARER_FILENAME, CREDENTIALS_FILENAME, SIGNIN_KEY, ACCOUNT_TOKEN_KEY


with open(CREDENTIALS_FILENAME, "r") as fh:
  creds_json = json.load(fh)

res = requests.post(
  f'https://identitytoolkit.googleapis.com/v1/accounts:signInWithCustomToken?key={creds_json[SIGNIN_KEY]}',
  headers={
    'origin': 'https://partiful.com',
  },
  data=json.dumps({
    "returnSecureToken": True,
    "token": creds_json[ACCOUNT_TOKEN_KEY],
  }),
)

data = json.loads(res.content.decode('utf-8'))

with open(BEARER_FILENAME, "w") as fh:
  fh.write(data["idToken"])
