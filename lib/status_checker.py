from lib.web_urls import WEBSITES
import requests
from datetime import datetime
import json

LOG_FILE = "website_status.log"
STATUS_FILE = "statuses.json"

def check_websites():
    statuses = {}
    with open(LOG_FILE, "a") as log:
        for url in WEBSITES:
            try:
                response = requests.get(url, timeout=8)
                status = "OK" if response.status_code == 200 else f"Error: {response.status_code}"
                log.write(f"{datetime.now().strftime('%d-%m-%Y %H:%M')} - URL: {url} - Status: {status}\n")
            except Exception as e:
                status = "DOWN"
                log.write(f"{datetime.now().strftime('%d-%m-%Y %H:%M')} - {url} - ERROR: {e}\n")

            statuses[url] = {"status": status, "last_checked": datetime.now().strftime("%d-%m-%Y %H:%M")}

        with open(STATUS_FILE, 'w') as file:
            json.dump(statuses, file, indent=4)
