from flask import Flask, render_template

from models.names_manager import NamesManager
from models.tracks_manager import TracksManager

app = Flask(__name__)

tracks_manager = TracksManager()
names_manager = NamesManager()


@app.route('/')
def hello():
    return 'Hello!!!'


@app.route('/names')
def unique_names():
    result = names_manager.unique_names()
    return f'Quantity: {result}'


@app.route('/tracks')
def tracks():
    result = tracks_manager.tracks()
    return f'Quantity: {result}'


@app.route('/tracks-sec')
def view_tracks():
    result = tracks_manager.view_tracks()
    return render_template('tracks.html', tracks=result)


if __name__ == '__main__':
    app.run()
