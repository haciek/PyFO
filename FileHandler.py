import shutil, logging
from pathlib import Path
from watchdog.events import FileSystemEvent, FileSystemEventHandler

from ConfigVar import *
from NotificationCenter import NotificationCenter as notify

class FileHandler(FileSystemEventHandler):
    def __init__(self) -> None:
        super().__init__()
        
    def on_any_event(self, event):
        if event.is_directory:
            return None

        with os.scandir(SOURCE_DIR) as entries: 
            for entry in entries:
                name = entry.name

                dest = self.__get_destination(name, entry.is_dir())
                if dest == None:
                    continue

                self.__move(name, dest)


    def __get_destination(self, name, is_dir) -> str | None:
        ext = f'.{name.split('.')[-1].lower()}'

        if ext in list(UNMOVABLE_EXT):
            return None

        # Skip Hidden Entries
        if name.startswith('.'):
            return None

        if is_dir:
            if os.path.join(SOURCE_DIR, name) in DIRS:
                print( os.path.join(SOURCE_DIR, name))
                return None
            return OTHER_DIR

        for link in LINKS:
            if ext in link[0]:
                return link[1]

        return OTHER_DIR



    def __move(self, filename, dir):
        if not os.path.exists(dir):
            Path(dir).mkdir(parents=True, exist_ok=True)
            logging.log(logging.INFO, f'Created destination directory at {dir}')

        source = os.path.join(SOURCE_DIR, filename)
        dest = os.path.join(dir, filename)
        
        # avoiding name duplication and overriding a file
        count = 0
        new_filename = ''
        while os.path.exists(dest):
            count += 1
            ext = filename.rfind('.')
            new_filename = f'{filename[:ext]}{count}{filename[ext:]}'
            dest = os.path.join(dir, new_filename)

        shutil.move(source, dest)

        notify.file_moved(filename, dest, new_filename)
        logging.log(logging.INFO, f'Moved \'{filename}\' -> \'{dir}\'{f' (renamed to {new_filename})' if new_filename != '' else ''}')

    def dispatch(self, event: FileSystemEvent) -> None:
        return super().dispatch(event)

