# iPhoto to Dropbox Importer

Copies photos from an iPhoto library to Dropbox. Photos will be stored in folders based on the iPhoto event album from which they came. Photos edited in iPhoto will be stored in an "/edits" subdirectory in each album folder.

## How to use

First change the file paths at the top of import.py
Then run:

`python import.py`

## TO DO:

* Should the file names be standardized? Perhaps all file names should just be the datetime that the picture was taken. This would make the ordering more explicit on the file system.
* Should user input be required before copying each album?
