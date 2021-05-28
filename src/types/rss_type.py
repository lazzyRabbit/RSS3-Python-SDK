#########################################
class IRSS3Content():
    def __init_(self) :   
        self.address = []
        self.mime_type = None
        self.name = None
        self.tags = []
        self.size_in_bytes = None
        self.duration_in_seconds = None

class IRSS3Context() :
    def __init_(self) :
        self.type = None
        self.list = []
        self.list_next = None

class IRSS3Item():
    def __init_(self) :
        super().__init_()

        self.authors = []
        self.title = None
        self.summary = None
        self.tags = []
        self.date_published = None
        self.date_modified = None

        self.type = None
        self.upstream = None

        self.contents = []

        self.signature = None

#########################################

class IRSS3Profile :
    def __init_(self) :
        self.name = None
        self.avatar = None
        self.bio = None
        self.tags = []
        self.signature = None

#########################################

class IRSS3Base :
    def __init_(self) :
        self.id = None
        self.date_created = 0
        self.date_updated = 0
        self.signature = None

#########################################
class IRSS3Link() :
    def __init_(self) :
        self.type = None
        self.tags = []
        self.list = []
        self.list_next = None
        self.signature = None

class IRSS3Backlink() :
    pass

class IRSS3Asset() :
    pass

class IRSS3(IRSS3Base):
    def __init_(self) :
        super().__init_()

        self.profile = None

        self.item = []
        self.items_next = None

        self.links = []             # IRSS3Link
        self.backlinks = []         # IRSS3Backlink
        self.assets = []            # IRSS3Asset

#########################################
class IRSS3Items(IRSS3Base) :
    def __init_(self) :
        self.items = []
        self.items_next = None

#########################################

class IRSS3List :
    pass

