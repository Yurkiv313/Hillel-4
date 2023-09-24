import sqlite3
from faker import Faker

from models.track import Track


class TracksManager:

    @staticmethod
    def create_table():
        conn = sqlite3.connect('mydatabase.db')
        cursor = conn.cursor()
        cursor.execute('''
             CREATE TABLE IF NOT EXISTS tracks (
             id INTEGER PRIMARY KEY,
             artist TEXT,
             length_trak INTEGER,
             release_date DATE
             )
         ''')
        fake = Faker()
        for _ in range(200):
            artist = fake.name()
            length_trak = fake.random_int(min=120, max=300)
            release_date = fake.past_date()
            cursor.execute('INSERT INTO tracks (artist, length_trak, release_date) VALUES (?, ?, ?)',
                           (artist, length_trak, release_date))
        conn.commit()

    @staticmethod
    def tracks():
        conn = sqlite3.connect('mydatabase.db')
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM tracks')
        count = cursor.fetchone()[0]
        if count == 0:
            TracksManager.create_table()
        else:
            query = "SELECT COUNT(artist) FROM tracks"
            cursor.execute(query)
            result = cursor.fetchone()
            k = result[0]
            conn.close()
            return k

    @staticmethod
    def view_tracks():
        conn = sqlite3.connect('mydatabase.db')
        cursor = conn.cursor()
        query = "SELECT id, artist, length_trak, release_date FROM tracks"
        cursor.execute(query)
        tracks = cursor.fetchall()
        conn.close()
        track_list = []
        # окремий клас для треку
        for track in tracks:
            track = Track(track[0], track[1], track[2], track[3])
            track_list.append(track)
        return track_list
