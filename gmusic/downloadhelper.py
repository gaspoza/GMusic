from client.client import Client
from config import *


class DownloadHelper:

    def __init__(self):
        self.client = Client()

    def download_playlist(self, playlist_name):
        if playlist_name is not None:
            playlist = self.client.get_playlist(playlist_name)
            folder = playlist_directory + '/' + playlist_name

            for track_id in playlist.tracks:
                self.client.download_track(track_id, folder, 'simple')

    def download_album(self, artist_name, album_name):
        if artist_name is not None:
            tracks = self.client.get_all_song()
            folder = library_directory + '/' + artist_name + '/' + album_name

            for track_id, track in tracks.items():
                if track.artist == artist_name and track.album == album_name:
                    self.client.download_track(track_id, folder, 'album')


if __name__ == '__main__':
    helper = DownloadHelper()

    #playlist_name = 'Electro'
    # playlist_name = 'Rock genere'
    playlist_name = 'Download'
    helper.download_playlist(playlist_name)

    # artist_name = 'Last Train'
    # album_name = 'Weathering'
    # helper.download_album(artist_name, album_name)
