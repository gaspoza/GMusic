

def get_simple_filename(song):
    return song.title.replace('/', '-')


def get_album_like_filename(song):
    track_number = song.track_number
    if track_number is None:
        return clean_special_characters(song.title)
    else:
        return clean_special_characters(str(track_number) + ' ' + song.title)


def clean_special_characters(filename):
    filename = filename.replace('/', '-')
    filename = filename.replace('?', '')
    return filename


FORMATTER_MAP = {'simple': get_simple_filename, 'album': get_album_like_filename}
