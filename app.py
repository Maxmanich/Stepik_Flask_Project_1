from flask import Flask, render_template

from data import title, subtitle, description, departures, tours


app = Flask(__name__)


@app.route('/')
def render_main():
    return render_template('index.html',
                           title=title,
                           tours=tours,
                           subtitle=subtitle,
                           description=description,
                           departures=departures)


@app.route('/departures/<departure>/')
def render_departures(departure):
    needed_tours = {}
    for tour_number, tour_info in tours.items():
        if tour_info.get('departure') == departure:
            needed_tours.update({tour_number: tour_info})

    return render_template('departure.html',
                           title=title,
                           departure=departure,
                           departures=departures,
                           tours=needed_tours)


@app.route('/tours/<id>/')
def render_tours(id):
    return render_template('tour.html',
                           title=title,
                           tour=tours.get(int(id)),
                           departures=departures)


if __name__ == '__main__':
    app.run()
