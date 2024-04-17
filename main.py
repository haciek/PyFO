from FileManager import *
import FileHandler

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
        format='%(asctime)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S')
    fm = FileManager(FileHandler.FileHandler())
    fm.run()
