import eyed3


class TagWriter:
    """
    TagWriter is the class handling the routing of writing IDv.x mp3 tag
    """

    def __init__(self, file_name):
        self._file = eyed3.load(file_name)
        self._file.initTag(version=(2, 4, 0))

    def write_title(self, title_name):
        self._file.tag.title = title_name

    def write_artist(self, artist_name):
        self._file.tag.artist = artist_name

    def write_album(self, album_name):
        self._file.tag.album = album_name

    def write_track_number(self, track_number):
        self._file.tag.track_num = track_number

    def save(self):
        self._file.tag.save()
