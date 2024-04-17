import logging, time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from FileHandler import FileHandler
from ConfigVar import SOURCE_DIR
from NotificationCenter import NotificationCenter as notify

class FileManager:
    def __init__(self, handler: FileSystemEventHandler) -> None:
        self.observer = Observer()
        self.event_handler = handler

    def run(self):
        event_handler = FileHandler()
        self.observer.schedule(event_handler, SOURCE_DIR, False)
        self.observer.start()

        notify.info(f'FileManager running in {SOURCE_DIR}')
        logging.log(logging.INFO, f'FileManager running in {SOURCE_DIR}')
        try:
            while True:
                time.sleep(10)
        except:
            self.observer.stop()
            notify.info('File Manager stopped')
            logging.log(logging.INFO, f'FileManager Stopped')

        self.observer.join()

