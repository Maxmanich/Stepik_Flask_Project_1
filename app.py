from flask import Flask
from flask import render_template
from data import *


app = Flask(__name__)


@app.route('/')
def render_main():
    return render_template('index.html', tours=tours, subtitle=subtitle, description=description)


@app.route('/departures/<departure>/')
def render_departures(departure):
    return render_template('departure.html', departure=departure, departures=departures, tours=tours)


@app.route('/tours/<id>/')
def render_tours(id):
    return render_template('tour.html', tour=tours.get(int(id)), departures=departures)


if __name__ == '__main__':
    app.run()
