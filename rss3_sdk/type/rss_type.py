#########################################
class IRSS3Content():
    def __init_(self, address = [], mime_type = None, name = None, tags = [], size_in_bytes = None, duration_in_seconds = None) :   
        self.address = []
        self.mime_type = mime_type
        self.name = name
        self.tags = tags
        self.size_in_bytes = size_in_bytes
        self.duration_in_seconds = duration_in_seconds

class IRSS3Context() :
    def __init_(self, type = None, list = [], list_next = None) :
        self.type = type
        self.list = list
        self.list_next = list_next

class IRSS3Item():
    def __init_(self, authors = [], title = None, summary = None, tags = [], date_published = None, date_modified = None, type = None, upstream = None, contents = [], a_contexts = [], signature = None) :
        self.authors = authors
        self.title = title
        self.summary = summary
        self.tags = tags
        self.date_published = date_published
        self.date_modified = date_modified

        self.type = type
        self.upstream = upstream

        self.contents = contents
        self.a_contexts = a_contexts

        self.signature = signature

#########################################

class IRSS3Profile :
    def __init_(self, name = None, avatar = None, bio = None, tags = [], signature = None) :
        self.name = name
        self.avatar = avatar
        self.bio = bio
        self.tags = tags
        self.signature = signature

#########################################

class IRSS3Base :
    def __init_(self, id = None, a_version = 'rss3.io/version/v0.1.0', date_created = 0, date_updated = 0, signature = None) :
        self.id = id
        self.a_version = a_version
        self.date_created = date_created
        self.date_updated = date_updated
        self.signature = signature

#########################################
class IRSS3Link() :
    def __init_(self, type = None, tags = [], list = [], list_next = None, signature = None) :
        self.type = type
        self.tags = tage
        self.list = list
        self.list_next = None
        self.signature = None

class IRSS3Backlink() :
    def __init_(self, type = None, list = [], next = None) :
        self.type = type
        self.list = list
        self.next = next

class IRSS3Asset() :
    def __init_(self, ) :
        self.type = None
        self.tags = []
        self.content = None

class IRSS3(IRSS3Base):
    def __init_(self, id = None, a_version = 'rss3.io/version/v0.1.0', date_created = 0, date_updated = 0, signature = None, \
                profile = None, item = [], items_next = None, links = [], a_backlinks = [], assets = []) :
        super().__init_(id, date_created, date_updated, signature)

        self.profile = profile

        self.item = item
        self.items_next = items_next

        self.links = links             # IRSS3Link
        self.a_backlinks = a_backlinks        # IRSS3Backlink
        self.assets = assets          # IRSS3Asset

#########################################
class IRSS3Items(IRSS3Base) :
    def __init_(self, id = None, a_version = 'rss3.io/version/v0.1.0', date_created = 0, date_updated = 0, signature = None, \
                items = [], items_next = None) :
        super().__init_(id, date_created, date_updated, signature)
        self.items = items
        self.items_next = items_next

#########################################

class IRSS3List :
    def __init_(self, id = None, list = [], next = None) :
        self.id = id
        
        self.list = list
        self.next = next

