import os, json
from flask import Flask, render_template, jsonify

from lib.status_checker import check_websites

app = Flask(__name__)

@app.route("/")
def index():
    try:
        status_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "statuses.json")
        with open(status_path, "r") as file:
            statuses = json.load(file)
        last_refreshed = list(statuses["social_media"].values())[0]["last_checked"]
        
    except FileNotFoundError:
            statuses = {"projects": {}, "social_media": {}}

    return render_template('index.html', statuses=statuses, last_refreshed=last_refreshed) 

@app.route("/refresh")
def refresh():
    check_websites()
    try:
        status_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "statuses.json")
        with open(status_path, "r") as file:
            statuses = json.load(file)
        last_refreshed = list(statuses["social_media"].values())[0]["last_checked"] if statuses["social_media"] else ""
    except FileNotFoundError:
        statuses = {"projects": {}, "social_media": {}}
        last_refreshed = ""
    return jsonify({"statuses": statuses, "last_refreshed": last_refreshed})

if __name__ == "__main__":
    app.run()