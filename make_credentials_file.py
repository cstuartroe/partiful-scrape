import json

from shared import CREDENTIALS_FILENAME, SIGNIN_KEY, ACCOUNT_TOKEN_KEY

signin_key = input("key: ")
account_token = input("token: ")

with open(CREDENTIALS_FILENAME, "w") as fh:
    json.dump(
        {
            SIGNIN_KEY: signin_key,
            ACCOUNT_TOKEN_KEY: account_token,
        },
        fh,
        indent=2,
        sort_keys=True,
    )
