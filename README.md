# partiful-scrape

This repo will allow you to download attendee CSVs from Partiful.

## Setup

Before you can download anything from Partiful, you need to perform some manual setup.

After downloading this repo, make sure you have a python environment set up and run `pip install -r requirements.txt`.

Navigate to Partiful in an incognito browser tab. Before logging in, use the inspect element function of your browser and open the network tab.

Next, log into Partiful as normal. Then in the network tab of the browser inspect tools, search for `accounts:signInWithCustomToken` like so:

![In the network tab, type accounts:signInWithCustomToken into the search bar](https://github.com/cstuartroe/partiful-scrape/raw/main/network_search.png)

Click the GET request (the one labeled `fetch`), not the OPTIONS request (the one labeled `preflight`). Look in the payload tab to find the key and token:

![In the network tab, type accounts:signInWithCustomToken into the search bar](https://github.com/cstuartroe/partiful-scrape/raw/main/payload_tab.png)

Run `python make_credentials_file.py`. This script will prompt you for the key and token. Paste them each from your browser inspect tool; the script will create a file called `credentials.txt`.

Once you have done this, run `python set_bearer.py`.
This stores a temporary Bearer token in `partiful_bearer.txt`;
you may need to rerun `python set_bearer.py` before later uses, as the Bearer token expires.

## Usage

Navigate to an event you are hosting on Partiful, then look at the URL in your browser.
It should look like `https://partiful.com/e/<some letters and numbers>`.
If you see a question mark `?` in the URL, ignore it and everything after it.

That string of letters and numbers is the event id. Copy it.

Then run `python download_csv.py <event id>`, replacing `<event id>` with the event id you copied from the browser URL. It will print the CSV in plain text to the output.

To get this into a CSV file, use `>` to pipe the output into a file.

For example, your whole command might look something like `python download_csv.py 7mfbkpRJxM8pPhDqc0zc > birthday_attendees.csv`
