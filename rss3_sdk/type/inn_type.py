class IInnContents :
    def __init__(self, address = None, mime_type = None, name = None, tags = [], size_in_bytes = None, duration_in_seconds = None) :
        self.address = address
        self.mime_type = mime_type
        self.name = name
        self.tags = tags
        self.size_in_bytes = size_in_bytes
        self.duration_in_seconds = duration_in_seconds

class IInnItem :
    def __init__(self, id = None, authors = [], title = None, summary = None, tags = None, type = None, upstream = None, contents = []) :
        self.id = id
        self.authors = authors
        self.title = title
        self.summary = summary
        self.tags = tags

        self.type = type
        self.upstream = upstream

        self.contents = contents    # IInnContents