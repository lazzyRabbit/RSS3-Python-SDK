class LocalStroge:
    def __init__(self):
        self._file_stroge_dict = dict()
        self._file_update_tag = set()

    def save_file(self, id, file):
        if id == None or file == None:
            raise ValueError("Id and file is invalid parameter")

        self._file_stroge_dict[id] = file

    def update_file(self, id ,file):
        if id == None or file == None:
            raise ValueError("Id and file is invalid parameter")

        self._file_stroge_dict[id] = file
        self._file_update_tag.add(id)

    def get_file(self, id):
        if id == None:
            raise ValueError("Id is invalid parameter")

        return self._file_stroge_dict[id]

    def refresh_all_modify_cache(self):
        self._file_update_tag.clear()

    def get_all_modify_cache(self):
        return self._file_update_tag

    def refresh_cache_set(self, cache_set):
        if isinstance(cache_set, set()) == False:
            raise ValueError("Cache_set is invalid parameter")

        self._file_update_tag.difference(cache_set)
