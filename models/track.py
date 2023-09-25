from dataclasses import dataclass


@dataclass
class Track:

    id: int
    artist: str
    length_trak: float
    release_date: str

    def __init__(self, id, artist, length_trak, release_date):
        self.id = id
        self.artist = artist
        self.length_trak = length_trak
        self.release_date = release_date

    def __str__(self):
        return f'{self.id} {self.artist} {self.length_trak} {self.release_date}'
