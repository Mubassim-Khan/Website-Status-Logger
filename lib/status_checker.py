from lib.web_urls import PERSONAL_PROJECTS, SOCIAL_MEDIA
import requests
from datetime import datetime
import json

LOG_FILE = "website_status.log"
STATUS_FILE = "statuses.json"

def check_websites():
    statuses = {"projects": {}, "social_media": {}}

    with open(LOG_FILE, "a") as log:
        for category, urls in [("projects", PERSONAL_PROJECTS), ("social_media", SOCIAL_MEDIA)]:
            for url in urls:
                try:
                    response = requests.get(url, timeout=8)
                    status = "OK" if response.status_code == 200 else f"Error: {response.status_code}"
                except Exception as e:
                    status = "DOWN"

                timestamp = datetime.now().strftime("%d-%m-%Y %H:%M")
                statuses[category][url] = {"status": status, "last_checked": timestamp}
                log.write(f"{timestamp} - URL: {url} - Status: {status}\n")

    with open(STATUS_FILE, "w") as file:
        json.dump(statuses, file, indent=4)