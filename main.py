import requests
import time
from datetime import datetime
import subprocess

# List of websites to check
WEBSITES = [
    "https://mubassim-khan.netlify.app"
    # "https://yourproject2.com",
    # "https://yourproject3.com"
]

LOG_FILE = "website_status.log"
COMMIT_INTERVAL = 300  # Time in seconds (same as logging or adjust as needed)

def check_websites():
    with open(LOG_FILE, "a") as log:
        for url in WEBSITES:
            try:
                response = requests.get(url, timeout=5)
                status = response.status_code
                log.write(f"{datetime.now()} - {url} - Status: {status}\n")
            except Exception as e:
                log.write(f"{datetime.now()} - {url} - ERROR: {e}\n")

def git_commit_and_push():
    """Commits and pushes the log file to GitHub."""
    try:
        subprocess.run(["git", "add", LOG_FILE], check=True)
        subprocess.run(["git", "commit", "-m", f"Auto log update {datetime.now()}"], check=True)
        subprocess.run(["git", "push"], check=True)
        print("Logs pushed to GitHub.")
    except subprocess.CalledProcessError as e:
        print(f"Git error: {e}")


if __name__ == "__main__":
    while True:
        check_websites()
        git_commit_and_push()
        time.sleep(COMMIT_INTERVAL)  # Wait for 5 minutes before running again
