class FileStroge :
    def __init_(self) :
        self.file_stroge_map = {}
        self.file_update_tag = {}
    
    def getFile(self, file_id) :
        return self.file_stroge_map.get(file_id)

    def strogeFile(self, file_id, file):
        self.file_stroge_map[file_id] = file
        self.file_update_tag.add(file_id)

    def patchFile(self, file_id) :
        self.file_update_tag.add(file_id)

    def updateFile(self, file_id) :
        self.file_update_tag.discard(file_id)

    def updateAll(self) :
        self.file_update_tag.clear()
        pass