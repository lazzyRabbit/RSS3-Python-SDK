import copy

class FileStroge :
    def __init_(self) :
        self.__file_stroge_dict = {}
        self.__file_update_tag = {}
    
    def getFile(self, file_id) :
        return self.__file_stroge_dict.get(file_id)

    def strogeFile(self, file_id, file):
        self.__file_stroge_dict[file_id] = file
        self.__file_update_tag.add(file_id)

    def patchFile(self, file_id) :
        self.__file_update_tag.add(file_id)

    def getAllUpdateFiles(self):
        curr_files_dict = {}
        for update_file_tag in self.file_update_tag :
            if update_file_tag in self.__file_stroge_dict :
                curr_files_dict[update_file_tag] = copy.deepcopy(self.__file_stroge_dict[update_file_tag])
        return curr_files_dict

    def updateFile(self, file_id) :
        self.__file_update_tag.discard(file_id)

    def updateAll(self) :
        self.__file_update_tag.clear()
        pass