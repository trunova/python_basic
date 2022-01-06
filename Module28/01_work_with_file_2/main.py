class File:
    """ Контекст-менеджер File """
    def __init__(self, name: str):
        self.fileName = name

    def __enter__(self):
        self.file = open(self.fileName, 'w+')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        self.file.close()
        if exc_type is FileExistsError:
            return True


with File('test.txt') as newFile:
    newFile.write('New file created\n')
