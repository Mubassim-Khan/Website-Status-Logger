from lib.web_urls import PERSONAL_PROJECTS, SOCIAL_MEDIA
import requests
from datetime import datetime
import json

LOG_FILE = "website_status.log"
STATUS_FILE = "statuses.json"

def check_websites():
    statuses = {"projects": {}, "social_media": {}}
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    
    with open(LOG_FILE, "a") as log:
        for category, sites in [("projects", PERSONAL_PROJECTS), ("social_media", SOCIAL_MEDIA)]:
            for site in sites:
                url = site["url"]
                name = site["name"]
                try:                
                    response = requests.get(url, timeout=15, headers=headers)
                    status = "OK" if response.status_code == 200 else f"Error: {response.status_code}"
                except Exception as e:
                    status = f"DOWN: ({e})"

                timestamp = datetime.now().strftime("%d-%m-%Y %H:%M")
                statuses[category][url] = {
                    "name": name,
                    "status": status, 
                    "last_checked": timestamp
                }
                log.write(f"{timestamp} - Name: {name} - URL: {url} - Status: {status}\n")

    with open(STATUS_FILE, "w") as file:
        json.dump(statuses, file, indent=4)