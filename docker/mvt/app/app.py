import os

from flask import Flask, render_template


mapbox_token = os.environ['MAPBOX_TOKEN']

app = Flask(__name__)

@app.route("/")
def index():

    return render_template('index.html', mapbox_token=mapbox_token)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)