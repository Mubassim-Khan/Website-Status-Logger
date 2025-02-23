from flask import Flask, render_template
import threading
import json
from background_logger import start_logging 

app = Flask(__name__)

# Start background logging in a separate thread
threading.Thread(target=start_logging, daemon=True).start()

@app.route('/')
def index():
    try:
        with open("statuses.json", "r") as file:
            statuses = json.load(file)
    except FileNotFoundError:
        statuses = {}

    return render_template('index.html', statuses = statuses)

if __name__ == '__main__':
    app.run(debug=True)
