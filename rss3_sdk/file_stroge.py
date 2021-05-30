class FileStroge :
    def __init_(self) :
        self.file_stroge_map = {}
        self.file_update_tag = {}
    
    def getFile(file_id) :
        return fileStrogeMap.get(file_id)

    def patchFile(file_id) :
        self.file_stroge_map[file_id] = file
        self.file_update_tag.add(file_id)

    def updateFile(file_id) :
        self.file_update_tag.discard(file_id)

    def updateAll() :
        self.fileUpdateTag.clear()
        pass