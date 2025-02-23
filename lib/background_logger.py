from lib.git_push import git_commit_and_push
from lib.status_checker import check_websites
import time
import threading

COMMIT_INTERVAL = 120  # Wait for 2 minutes before running again

log_lock = threading.Lock()

def start_logging():
    while True:
        with log_lock:
            check_websites()
            git_commit_and_push()
        time.sleep(COMMIT_INTERVAL) 
