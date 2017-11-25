class Playlist:
    """
        Playlist class
    """

    def __init__(self, playlist_id, name):
        self.id = playlist_id
        self.name = name
        self.tracks = {}

    def __str__(self):
        return '%s %s (track ids : %s)' % (self.id, self.name, self.tracks)
