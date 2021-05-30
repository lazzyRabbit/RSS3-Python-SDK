import type.rss_type

class Converter :
    def __init_(self) :
        pass

    @staticmethod
    def json2IRSS3Content(data) :
        pass

    @staticmethod
    def iRSS3Content2Json(data) :
        pass
    
    @staticmethod
    def json2IRSS3Context(data) :
        pass
    
    @staticmethod
    def iRSS3Context2Json(data) :
        pass

    @staticmethod
    def json2IRSS3Profile(data) :
        profile = type.rss_type.IRSS3Profile()

        profile.name = data.get('name')
        profile.avatar = data.get('avatar')
        profile.bio = data.get('bio')
        profile.tags = data.get('tags')
        profile.signature = data.get('signature')

        return profile

    @staticmethod
    def iRSS3Profile2Json(data) :
        pass

    @staticmethod
    def json2IRSS3Link(data) :
        link = type.rss_type.IRSS3Link()

        link.type = data.get('type')
        link.tags = data.get('tage')
        link.list = data.get('list')
        link.list_next = 
        link.signature = data.get('signature')
        
        return link
    
    @staticmethod
    def iRSS3Link2Json(data) :
        pass
    
    @staticmethod
    def json2IRSS3Backlink(data) :
        
        pass
    
    @staticmethod
    def iRSS3Backlink2Json(data) :
        pass
    
    @staticmethod
    def json2IRSS3Asset(data) :
        
        pass
    
    @staticmethod
    def iRSS3Asset2Json(data) :
        pass

    @staticmethod
    def json2IRSS3(data) :
        irss3 = type.rss_type.IRSS3()
        
        irss3.id = data.get('id')
        irss3.a_version = data.get('@version')
        irss3.date_created = data.get('date_created')
        irss3.date_updated = data.get('date_updated')
        irss3.signature = data.get('signature')

        l_profile = []
        l_links = []
        l_backlinks = []
        l_assets = []

        if 'profile' in data :
            for profile_content in data['profile'] :
                l_profile.append(Converter.json2IRSS3Profile(profile_content))
        irss3.profile = l_profile

        if 'links' in data :
            for link_content in data['links'] :
                l_links.append(Converter.json2IRSS3Link(link_content))
        irss3.links = l_links

        if '@backlinks' in data :
            for backlink_content in data['@backlinks'] :
                l_backlinks.append(Converter.json2IRSS3Backlink(backlink_content))
        irss3.a_backlinks = l_backlinks

        if 'asset' in data :
            for backlink_content in data['assert'] :
                l_assets.append(Converter.json2IRSS3Asset(backlink_content))
        irss3.assets = l_assets


        return irss3

    @staticmethod
    def iRSS32Json(data) :

        pass
    
    @staticmethod
    def json2IRSS3List(data) :
        pass

    @staticmethod
    def iRSS3List2Json(data) :
        pass