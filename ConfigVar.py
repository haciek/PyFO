import os

USER = os.environ.get('USER')
SOURCE_DIR =    f'/Users/{USER}/Downloads'
OTHER_DIR =     f'/Users/{USER}/Downloads/Other'

VIDEO_DIR =     f'/Users/{USER}/Downloads/Movies'
MUSIC_DIR =     f'/Users/{USER}/Downloads/Music'
IMAGE_DIR =     f'/Users/{USER}/Downloads/Pictures'
DOCUMENT_DIR =  f'/Users/{USER}/Downloads/Documents'
CODE_DIR =      f'/Users/{USER}/Downloads/Code'
ARCHIVE_DIR =   f'/Users/{USER}/Downloads/Archives'
ISO_DIR =       f'/Users/{USER}/Downloads/Disk Images'
TORRENT_DIR =   f'/Users/{USER}/Downloads/Torrents'
APP_DIR =       f'/Users/{USER}/Downloads/Apps'

IMAGE_EXT =     ('.jpeg', '.jpg', '.png', '.gif', '.tiff', '.tif', '.bmp', '.svg', '.raw', '.psd', '.ai', '.eps', '.webp', '.ico', '.cr2', '.nef', '.orf', '.dng', '.arw', '.pict', '.heic', '.heif')
MUSIC_EXT =     ('.mp3', '.wav', '.aiff', '.aac', '.flac', '.ogg', '.midi', '.wma', '.amr', '.m4a', '.alac', '.ape', '.ac3', '.dsd', '.pcm', '.mp2')
VIDEO_EXT =     ('.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm', '.mpeg', '.3gp', '.ogv', '.ts', '.m4v', '.rm', '.rmvb', '.vob')
DOCUMENT_EXT =  ('.doc', '.docx', '.pdf', '.txt', '.rtf', '.odt', '.xls', '.xlsx', '.csv', '.ppt', '.pptx', '.odp', '.ods' )
CODE_EXT =      ('.py', '.java', '.cpp', '.c', '.cs', '.js', '.html', '.css', '.php', '.r', '.swift', '.go', '.ts', '.ruby', '.scala', '.kotlin', '.objectivec', '.perl', '.lua', '.bash')
ARCHIVE_EXT =   ('.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.xz', '.tar.gz', '.tar.bz2', '.tar.xz')
ISO_EXT =       ('.iso')
TORRENT_EXT =   ('.torrent')
APP_EXT =       ('.exe', '.dmg', '.deb', '.rpm', '.app', '.apk')


UNMOVABLE_EXT = ('.ini', '.bin')

DIRS = [OTHER_DIR, SOURCE_DIR, VIDEO_DIR, MUSIC_DIR, IMAGE_DIR, DOCUMENT_DIR, CODE_DIR, ARCHIVE_DIR, ISO_DIR, TORRENT_DIR, APP_DIR]

LINKS = [
    (VIDEO_EXT, VIDEO_DIR),
    (IMAGE_EXT, IMAGE_DIR),
    (DOCUMENT_EXT, DOCUMENT_DIR),
    (MUSIC_EXT, MUSIC_DIR),
    (CODE_EXT, CODE_DIR),
    (ARCHIVE_EXT, ARCHIVE_DIR),
    (TORRENT_EXT, TORRENT_DIR),
    (APP_EXT, APP_DIR),
    (ISO_EXT, ISO_DIR),
]
