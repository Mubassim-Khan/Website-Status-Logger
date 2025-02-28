from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("/")
def index():
    try:
        with open("statuses.json", "r") as file:
            statuses = json.load(file)
    except FileNotFoundError:
            statuses = {"projects": {}, "social_media": {}}

    return render_template('index.html', statuses = statuses) 

if __name__ == "__main__":
    app.run()
