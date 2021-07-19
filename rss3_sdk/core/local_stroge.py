from . import (
    base_stroge
)

class LocalStroge(base_stroge.BaseStroge):
    def __init__(self):
        self._file_stroge_dict = dict()

    def save_file(self, id, file):
        if id == None or file == None:
            raise ValueError("Id and file is invalid parameter")

        self._file_stroge_dict[id] = file

    def get_file(self, id):
        if id == None:
            raise ValueError("Id is invalid parameter")

        return self._file_stroge_dict[id]