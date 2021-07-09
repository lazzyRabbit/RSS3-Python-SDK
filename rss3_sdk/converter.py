from rss3_sdk.type import rss3_type
from rss3_sdk.type import inn_type
from marshmallow import Schema, fields, post_load

# rss3 json converter
#########################################
class IRSS3ContentSchema(Schema) :
    address = fields.List(fields.String, data_key = 'address', required = True)
    mime_type = fields.String(data_key = 'mime_type', required = True)
    name = fields.String(data_key = 'name')
    tags = fields.List(fields.String, data_key = 'tags')
    size_in_bytes = fields.String(data_key = 'size_in_bytes')
    duration_in_seconds = fields.String(data_key = 'duration_in_seconds')

    @post_load
    def make_content(self, data, **kwargs):
        return rss3_type.IRSS3Content(**data)

class IRSS3ContextSchema(Schema) :
    type = fields.String(data_key = 'type')
    list = fields.List(fields.String, data_key = 'list', required = True)
    list_next = fields.String(data_key = 'list_next')

    @post_load
    def make_context(self, data, **kwargs):
        return rss3_type.IRSS3Context(**data)

class IRSS3ItemSchema(Schema):
    id = fields.String(data_key = 'id', required = True)
    authors = fields.List(fields.String, data_key = 'authors')
    title = fields.String(data_key = 'title')
    summary = fields.String(data_key = 'summary')
    tags = fields.List(fields.String, data_key = 'tags')
    date_published = fields.String(data_key = 'date_published')
    date_modified = fields.String(data_key = 'date_modified')

    type = fields.String(data_key = 'type')
    upstream = fields.String(data_key = 'upstream')

    contents = fields.List(fields.Nested(IRSS3ContentSchema), data_key = 'contents')
    a_contexts = fields.List(fields.Nested(IRSS3ContextSchema), data_key = '@contexts')

    signature = fields.String(data_key = 'signature', required = True)

    @post_load
    def make_item(self, data, **kwargs):
        return rss3_type.IRSS3Item(**data)

class IRSS3ProfileSchema(Schema) :
    name = fields.String(data_key = 'name')
    avatar = fields.List(fields.String, data_key = 'avatar', required = False)
    bio = fields.String(data_key = 'bio', required = False)
    tags = fields.List(fields.String, data_key = 'tags', required = False)
    signature = fields.String(data_key = 'signature', required = True)

    @post_load
    def make_profile(self, data, **kwargs):
        return rss3_type.IRSS3Profile(**data)

class IRSS3LinkSchema(Schema) :
    type = fields.String(data_key = 'type', required = True)
    tags = fields.List(fields.String, data_key = 'tags')
    list = fields.List(fields.String, data_key = 'list', required = True)
    list_next = fields.String(data_key = 'list_next')
    signature = fields.String(data_key = 'signature', required = True)

    @post_load
    def make_link(self, data, **kwargs):
        return rss3_type.IRSS3Link(**data)

class IRSS3BacklinkSchema(Schema) :
    type = fields.String(data_key = 'type', required = True)
    list = fields.List(fields.String, data_key = 'list', required = True)
    list_next = fields.String(data_key = 'list_next')

    @post_load
    def make_backlink(self, data, **kwargs):
        return rss3_type.IRSS3Backlink(**data)

class IRSS3AssetSchema(Schema) :
    type = fields.String(data_key = 'type', required = True)
    tags = fields.List(fields.String, data_key = 'tags')
    content = fields.String(data_key = 'content', required = True)

    @post_load
    def make_asset(self, data, **kwargs):
        return rss3_type.IRSS3Asset(**data)

class IRSS3IndexSchema(Schema):
    id = fields.String(data_key = 'id', required = True)
    a_version = fields.String(data_key = '@version', required = True)
    date_created = fields.String(data_key = 'date_created', required = True)
    date_updated = fields.String(data_key = 'date_updated', required = True)
    signature = fields.String(data_key = 'signature', required = True)

    profile = fields.Nested(IRSS3ProfileSchema, data_key = 'profile')

    items = fields.List(fields.Nested(IRSS3ItemSchema), data_key = 'items')
    items_next = fields.String(data_key = 'items_next')

    links = fields.List(fields.Nested(IRSS3LinkSchema, data_key = 'links'))
    a_backlinks = fields.List(fields.Nested(IRSS3BacklinkSchema), data_key = '@backlinks')
    assets = fields.List(fields.Nested(IRSS3AssetSchema, data_key = 'assets'))

    @post_load
    def make_index(self, data, **kwargs):
        return rss3_type.IRSS3Index(**data)

class IRSS3ItemsSchema(Schema) :
    id = fields.String(data_key = 'id', required = True)
    a_version = fields.String(data_key = '@version', required = True)
    date_created = fields.String(data_key = 'date_created', required = True)
    date_updated = fields.String(data_key = 'date_updated', required = True)
    signature = fields.String(data_key = 'signature', required = True)
    
    items = fields.Nested(IRSS3ItemSchema, data_key = 'item', required = True)
    items_next = fields.String(data_key = 'items_next', required = True)

    @post_load
    def make_items(self, data, **kwargs):
        return rss3_type.IRSS3Items(**data)

class IRSS3ListSchema(Schema) :
    id = fields.String(data_key = 'id', required = True)
    
    list = fields.List(fields.String, data_key = 'list', required = True)
    next = fields.String(data_key = 'next', required = True)

    @post_load
    def make_list(self, data, **kwargs):
        return rss3_type.IRSS3List(**data)

# inn json converter
#########################################
class IInnProfileSchema(Schema) :
    name = fields.String(data_key='name', required = False)
    avatar = fields.List(fields.String, data_key='avatar', required = False)
    bio = fields.String(data_key='bio', required = False)
    tags = fields.List(fields.String, data_key='tags', required = False)

    @post_load
    def make_profile(self, data, **kwargs):
        return rss3_type.IRSS3Profile(**data)

class IInnItemSchema(Schema) :
    id = fields.String(data_key = 'id', required = True)
    authors = fields.List(fields.String, data_key = 'authors')
    title = fields.String(data_key = 'title')
    summary = fields.String(data_key = 'summary')
    tags = fields.List(fields.String, data_key = 'tags')

    type = fields.String(data_key = 'type')
    upstream = fields.String(data_key = 'upstream')

    contents = fields.List(fields.Nested(IRSS3ContentSchema), data_key = 'contents')

    signature = fields.String(data_key = 'signature', required = True)

    @post_load
    def make_item(self, data, **kwargs):
        return inn_type.IInnItem(**data)

