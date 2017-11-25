class Track:
    """
        Track class
    """

    def __init__(self, track_id, title, artist, album, track_number):
        self.id = track_id
        self.title = title
        self.artist = artist
        self.album = album
        self.track_number = track_number

    def __str__(self):
        return '%s : %s - %s (%s -  %s)' % (self.id, self.title, self.artist, self.album, self.track_number)
