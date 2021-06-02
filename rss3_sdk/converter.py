import copy
from marshmallow import Schema, fields, ValidationError

# json converter
#########################################
class IRSS3ContentSchema() :
    address = fields.List(fields.String, attribute = 'address')
    mime_type = fields.String(attribute = 'mime_type')
    name = fields.String(attribute = 'name')
    tags = fields.String(attribute = 'name')
    size_in_bytes = fields.String(attribute = 'size_in_bytes')
    duration_in_seconds = fields.String(attribute = 'duration_in_seconds')

class IRSS3ContextSchema() :
    type = fields.String(attribute = 'type')
    list = fields.List(fields.String, attribute = 'list')
    list_next = fields.String(attribute = 'list_next')

class IRSS3ItemSchema():
    id = fields.String(attribute = 'id')
    authors = fields.String(attribute = 'authors')
    title = fields.String(attribute = 'title')
    summary = fields.String(attribute = 'summary')
    tags = fields.List(fields.String, attribute = 'tags')
    date_published = fields.String(attribute = 'date_published')
    date_modified = fields.String(attribute = 'date_modified')

    type = fields.String(attribute = 'type')
    upstream = fields.String(attribute = 'upstream')

    contents = fields.List(fields.Nested(IRSS3ContentSchema, attribute = 'contents'))
    a_contexts = fields.List(fields.Nested(IRSS3ContextSchema, attribute = '@contexts'))

    signature = fields.String(attribute = 'signature')

class IRSS3ProfileSchema() :
    name = fields.String(attribute = 'name')
    avatar = fields.String(attribute = 'avatar')
    bio = fields.String(attribute = 'bio')
    tags = fields.List(fields.String, attribute = 'tags')
    signature = fields.String(attribute = 'signature')

class IRSS3LinkSchema() :
    type = fields.String(attribute = 'type')
    tags = fields.List(fields.String, attribute = 'tags')
    list = fields.List(fields.String, attribute = 'list')
    list_next = fields.String(attribute = 'list_next')
    signature = fields.String(attribute = 'signature')

class IRSS3BacklinkSchema() :
    type = fields.String(attribute = 'type')
    list = fields.List(fields.String, attribute = 'list')
    list_next = fields.String(attribute = 'list_next')

class IRSS3AssetSchema() :
    type = fields.String(attribute = 'type')
    tags = fields.List(fields.String, attribute = 'tags')
    content = fields.String(attribute = 'content')

class IRSS3Schema():
    id = fields.String(attribute = 'id')
    a_version = fields.String(attribute = '@version')
    date_created = fields.String(attribute = 'date_created')
    date_updated = fields.String(attribute = 'date_updated')
    signature = fields.String(attribute = 'signature')

    profile = fields.Nested(IRSS3ProfileSchema, attribute = 'profile')

    items = fields.Nested(IRSS3ItemSchema, attribute = 'item')
    items_next = fields.String(items_next)

    links = fields.List(fields.Nested(IRSS3BacklinkSchema, attribute = 'links'))
    a_backlinks = fields.List(fields.Nested(IRSS3BacklinkSchema, attribute = '@backlinks'))
    assets = fields.List(fields.Nested(IRSS3AssetSchema, attribute = 'assets'))

class IRSS3ItemsSchema() :
    id = fields.String(attribute = 'id')
    a_version = fields.String(attribute = '@version')
    date_created = fields.String(attribute = 'date_created')
    date_updated = fields.String(attribute = 'date_updated')
    signature = fields.String(attribute = 'signature')
    
    items = fields.Nested(IRSS3ItemSchema, attribute = 'item')
    items_next = fields.String(items_next)

class IRSS3ListSchema() :
    id = fields.String(attribute = 'id')
    
    list = fields.List(fields.String, attribute = 'list')
    next = fields.String(attribute = 'next')

# inn converter
#########################################

def IInnContentsDeepCopy2Content(inn_content, i_rss3_contetnt) :
    i_rss3_contetnt.address = copy.deepcopy(inn_item.address)
    i_rss3_contetnt.mime_type = copy.deepcopy(inn_item.mime_type)
    i_rss3_contetnt.name = copy.deepcopy(inn_item.name)
    i_rss3_contetnt.tags = copy.deepcopy(inn_item.tags)
    i_rss3_contetnt.duration_in_seconds = copy.deepcopy(inn_item.duration_in_seconds)

def IInnItemDeepCopy2IRSS3Item(inn_item, i_rss3_item) :
    i_rss3_item.id = copy.deepcopy(inn_item.id)
    i_rss3_item.authors = copy.deepcopy(inn_item.authors)
    i_rss3_item.title = copy.deepcopy(inn_item.title)
    i_rss3_item.summary = copy.deepcopy(inn_item.summary)
    i_rss3_item.tags = copy.deepcopy(inn_item.tags)
    i_rss3_item.date_published = copy.deepcopy(inn_item.date_published)
    i_rss3_item.date_modified = copy.deepcopy(inn_item.date_modified)

    i_rss3_item.type = copy.deepcopy(inn_item.type)
    i_rss3_item.upstream = copy.deepcopy(inn_item.upstream)

    
    pass