from os.path import getmtime
import plistlib

LIBRARY_FOLDER = "/Users/Quinn/Pictures/iPhoto Library 2/"
ALBUM_DATA_FILE = "AlbumData.xml"

album_data = plistlib.readPlist(LIBRARY_FOLDER + ALBUM_DATA_FILE)

albums = album_data['List of Albums']
albums = [album for album in albums if album['Album Type'] == 'Event']

photos = album_data['Master Image List']

albums_to_copy = {}
for album in albums:
	# print "{} --- {} --- {}".format(album['AlbumName'], len(album['KeyList']), album['Album Type'])
	album_photos = {
		photo: {
			photos[photo]['ImagePath']
		} for photo in album['KeyList'] if photo in photos
	}

	albums_to_copy[album['GUID']] = {
		'name': album['AlbumName'],
		'photos': album_photos,
		'date': min([getmtime(photo) for photo in album_photos.values()])
	}
	# for photo in album['KeyList']:
	# 	print "###", photos[photo]['ImagePath']




for key, value in masterImageList.items():
    print (value['ImagePath'])