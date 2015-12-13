from os.path import getmtime
from os import mkdir
import plistlib
from re import sub
from shutil import copy
from time import gmtime, strftime

LIBRARY_FOLDER = '/Users/Quinn/Pictures/iPhoto Library 2/'
DROPBOX_FOLDER = '/Users/Quinn/Dropbox/photos/'
ALBUM_DATA_FILE = 'AlbumData.xml'

album_data = plistlib.readPlist(LIBRARY_FOLDER + ALBUM_DATA_FILE)

albums = [
    album for album in album_data['List of Albums']
    if album['Album Type'] == 'Event'
]
photos = album_data['Master Image List']

albums_to_copy = {}
for album in albums:
    album_photos = {
        photo: {
            'current': photos[photo]['ImagePath'],
            'original': photos[photo].get('OriginalPath'),
        } for photo in album['KeyList'] if photo in photos
    }
    originals = [photo['original'] or photo['current'] for photo_id, photo in album_photos.items()]
    edits = [photo['current'] for photo_id, photo in album_photos.items() if photo['original'] is not None]
    album_date = strftime('%Y_%m_%d', gmtime(min([getmtime(photo) for photo in originals])))
    album_name = "{}_{}".format(album_date, sub(r'\s+', '_', album['AlbumName'].lower()))

    album_folder = DROPBOX_FOLDER + album_name

    print "#### Album: {} --- photos: {} --- edits {}".format(album_name, len(originals), len(edits))

    mkdir(album_folder)
    for photo in originals:
        copy(photo, album_folder)

    for photo in edits:
        copy(photo, album_folder + '/edits/')

    print "done."
