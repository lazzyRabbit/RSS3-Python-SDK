import copy

#########################################
class IRSS3Content():
    def __init__(self, address = [], mime_type = None, name = None, tags = [], size_in_bytes = None, duration_in_seconds = None) :   
        self.address = address
        self.mime_type = mime_type
        self.name = name
        self.tags = tags
        self.size_in_bytes = size_in_bytes
        self.duration_in_seconds = duration_in_seconds

class IRSS3Context() :
    def __init__(self, type = None, list = [], list_next = None) :
        self.type = type
        self.list = list
        self.list_next = list_next

class IRSS3Item():
    def __init__(self, id = None, authors = [], title = None, summary = None, tags = [], date_published = None, date_modified = None, type = None, upstream = None, contents = [], a_contexts = [], signature = None) :
        self.id = id
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

class IRSS3Profile() :
    def __init__(self, name = None, avatar = None, bio = None, tags = [], signature = None) :
        self.name = name
        self.avatar = avatar
        self.bio = bio
        self.tags = tags
        self.signature = signature

#########################################

class IRSS3Base() :
    def __init__(self, id = None, a_version = 'rss3.io/version/v0.1.0', date_created = 0, date_updated = 0, signature = None) :
        self.id = id
        self.a_version = a_version
        self.date_created = date_created
        self.date_updated = date_updated
        self.signature = signature

#########################################
class IRSS3Link() :
    def __init__(self, type = None, tags = [], list = [], list_next = None, signature = None) :
        self.type = type
        self.tags = tags
        self.list = list
        self.list_next = list_next
        self.signature = signature

class IRSS3Backlink() :
    def __init__(self, type = None, list = [], next = None) :
        self.type = type
        self.list = list
        self.next = next

class IRSS3Asset() :
    def __init__(self, type = None, tags = [], content = None) :
        self.type = type
        self.tags = tags
        self.content = content

class IRSS3Index(IRSS3Base):
    def __init__(self, id = None, a_version = 'rss3.io/version/v0.1.0', date_created = 0, date_updated = 0, signature = None, \
                profile = None, items = [], items_next = None, links = [], a_backlinks = [], assets = []) :
        super().__init__(id, a_version, date_created, date_updated, signature)

        self.profile = profile

        self.items = items
        self.items_next = items_next

        self.links = links                    # IRSS3Link
        self.a_backlinks = a_backlinks        # IRSS3Backlink
        self.assets = assets                  # IRSS3Asset

#########################################
class IRSS3Items(IRSS3Base) :
    def __init__(self, id = None, a_version = 'rss3.io/version/v0.1.0', date_created = 0, date_updated = 0, signature = None, \
                items = [], items_next = None) :
        super().__init__(id, a_version, date_created, date_updated, signature)
        self.items = items
        self.items_next = items_next

#########################################

class IRSS3List :
    def __init__(self, id = None, list = [], next = None) :
        self.id = id
        
        self.list = list
        self.next = next