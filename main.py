from flask import Flask, render_template
import threading
from background_logger import start_logging 

app = Flask(__name__)

# Start background logging in a separate thread
threading.Thread(target=start_logging, daemon=True).start()

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=False)
