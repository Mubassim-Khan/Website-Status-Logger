# Might delete this file later, as it is of no use

from lib.git_push import git_commit_and_push
from lib.status_checker import check_websites

def start_logging():
    check_websites()
    git_commit_and_push()

start_logging()