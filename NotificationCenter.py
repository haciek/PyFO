import subprocess

class NotificationCenter(object):
    __CMD = '''
    on run argv
    display notification (item 3 of argv) subtitle (item 2 of argv) with title (item 1 of argv)
    end run
    '''
    @classmethod
    def __notify(cls, subtitle, text):
        title = 'File Manager'
        subprocess.call(['osascript', '-e', cls.__CMD, title, subtitle, text])

    @classmethod
    def file_moved(cls, filename, dest, renamed_to=''):
        subtitle = 'File Moved'
        was_renamed = f' (renamed to \'{renamed_to}\')' if renamed_to == '' else ''
        text = f'{filename} moved to {dest}{was_renamed}'
        cls.__notify(subtitle, text)

    @classmethod
    def info(cls, text):
        subtitle = 'Info'
        cls.__notify(subtitle, text)
