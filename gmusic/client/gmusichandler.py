import urllib.request

from client.track import Track
from gmusicapi import Mobileclient

from client.playlist import Playlist


class GMusicHandler:
    """
    GMusicHandler is the class handling the communication with the google music api.
    """

    def __init__(self, user, password):
        self.user = user
        self.password = password

        self.api = Mobileclient()
        if not self.api.login(user, password, Mobileclient.FROM_MAC_ADDRESS):
            raise Exception('Failed to login...')

        self.tracks = {}
        self.playlists = {}

    def get_all_song(self):
        if len(self.tracks) == 0:
            songs = self.api.get_all_songs()
            for song in songs:
                track_id = song['id']
                title = song['title']
                artist = song['artist']
                album = song['album']
                track_number = song['trackNumber']

                self.tracks[track_id] = Track(track_id, title, artist, album, track_number)
        return self.tracks

    def get_song(self, track_id):
        songs = self.get_all_song()
        return songs.get(track_id)

    def get_all_playlist(self):
        if len(self.playlists) == 0:
            playlists = self.api.get_all_user_playlist_contents()
            for pl in playlists:
                playlist = self._build_playlist(pl)
                self.playlists[playlist.id] = playlist
        return self.playlists

    def _build_playlist(self, data):
        playlist_id = data['id']
        playlist_name = data['name']
        p = Playlist(playlist_id, playlist_name)
        for track in data['tracks']:
            track_id = track['trackId']
            source = track['source']
            if source == '1':
                song = self.get_song(track_id)
                p.tracks[song.id] = song
            elif source == '2':
                song = self._create_track(track_id, track['track'])
                p.tracks[song.id] = song

        return p

    def _create_track(self, track_id, data):
        title = data['title']
        artist = data['artist']
        album = data['album']
        track_number = data['trackNumber']
        song = Track(track_id, title, artist, album, track_number)
        self.tracks[song.id] = song
        return song

    def get_playlist(self, playlist_name):
        playlists = self.get_all_playlist()
        return next(iter([p for p in playlists.values() if p.name == playlist_name]), None)

    def download_track(self, track_id):
        url = self.api.get_stream_url(track_id)
        file_path, headers = urllib.request.urlretrieve(url)
        return file_path

    def search(self, query):
        return self.api.search(query)


if __name__ == '__main__':
    playlist_name = 'Electro'

    client = GMusicHandler()
    playlist = client.get_playlist(playlist_name)
    print(playlist)

    track_id = playlist.tracks[0]
    print(track_id)
