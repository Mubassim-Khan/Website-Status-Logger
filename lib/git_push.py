# Might delete this file later, as it is of no use

from datetime import datetime
import subprocess

LOG_FILE = "website_status.log"
STATUS_FILE = "statuses.json"

def git_commit_and_push():
    """Commits and pushes the log file to GitHub."""
    try:
        subprocess.run(["git", "add", LOG_FILE, STATUS_FILE], check=True)
        subprocess.run(["git", "commit", "-m", f"[Auto Commit] - Log & Status Update at {datetime.now().strftime('%A, %d-%m-%Y, %H:%M:%S')}"], check=True)
        subprocess.run(["git", "push"], check=True)
        subprocess.run(["git", "push", "--set-upstream", "origin", "main"], check=True)
        print(f"Files commited and pushed to GitHub at {datetime.now().strftime('%H:%M')}.\n")
    except subprocess.CalledProcessError as e:
        print(f"Git error: {e}")
