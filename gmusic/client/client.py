import os

from gmusic.filesystem.storagemanager import StorageManager

from gmusic.client.gmusichandler import GMusicHandler
from gmusic.config import *
from gmusic.filesystem.formatter import FORMATTER_MAP
from gmusic.tag.tagwriter import TagWriter


class Client:
    """
    Client is the class coordinating the interaction between Google Music API,
    the storage manager and the IDv.x mp3 tagger.
    """

    def __init__(self, user=google_account, password=google_password):
        self.user = user
        self.password = password
        self._cache_directory = cache_directory

        self._gmusic_handler = GMusicHandler(user, password)
        self._sm = StorageManager()

    def get_all_song(self):
        return self._gmusic_handler.get_all_song()

    def get_playlist(self, playlist_name):
        return self._gmusic_handler.get_playlist(playlist_name)

    def download_track(self, track_id, folder_name, formatter_type='simple'):
        filename_in_cache = self._save_track_in_cache(track_id)
        filename = self._move(track_id, filename_in_cache, folder_name)

        # Retrieve metadata
        song = self._gmusic_handler.get_song(track_id)

        self._set_metadata(filename, song)
        self._rename(filename, folder_name, formatter_type, song)

    def _save_track_in_cache(self, track_id):
        filename_in_cache = track_id + '.mp3'
        src = os.path.join(self._cache_directory, filename_in_cache)
        if not self._sm.has_file(src):
            tmp_file = self._gmusic_handler.download_track(track_id)
            self._sm.rename(tmp_file, src)
        return src

    def _move(self, track_id, track_path, folder_name):
        self._sm.create_directory_if_not_existing(folder_name)
        dst = os.path.join(folder_name, track_id + '.mp3')
        self._sm.copy_file(track_path, dst)
        return dst

    @staticmethod
    def _set_metadata(filename, song):
        tagger = TagWriter(filename)
        tagger.write_title(song.title)
        tagger.write_artist(song.artist)
        tagger.write_album(song.album)
        tagger.write_track_number(song.track_number)
        tagger.save()

    def _rename(self, source, destination_folder, formatter_type, song):
        file_name = FORMATTER_MAP[formatter_type](song)
        new_file = os.path.join(destination_folder, file_name + '.mp3')
        self._sm.rename(source, new_file)

    def search(self, query):
        return self._gmusic_handler.search(query)
