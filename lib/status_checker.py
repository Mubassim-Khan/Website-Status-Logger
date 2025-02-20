from web_urls import WEBSITES
import requests
from datetime import datetime

LOG_FILE = "website_status.log"

def check_websites():
    with open(LOG_FILE, "a") as log:
        for url in WEBSITES:
            try:
                response = requests.get(url, timeout=5)
                status = response.status_code
                log.write(f"{datetime.now().strftime('%d-%m-%Y %H:%M')} - URL: {url} - Status: {status}\n")
            except Exception as e:
                log.write(f"{datetime.now().strftime('%d-%m-%Y %H:%M')} - {url} - ERROR: {e}\n")
