class IInnProfile() :
    def __init__(self, name=None, avatar=None, bio=None, tags=[], signature=None):
        self.name = name
        self.avatar = avatar
        self.bio = bio
        self.tags = tags

class IInnItem() :
    def __init__(self, id = None, authors = [], title = None, summary = None, tags = [], type = None, upstream = None, contents = []) :
        self.id = id
        self.authors = authors
        self.title = title
        self.summary = summary
        self.tags = tags

        self.type = type
        self.upstream = upstream

        self.contents = contents