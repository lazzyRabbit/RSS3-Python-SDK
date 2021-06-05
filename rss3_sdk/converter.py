from marshmallow import Schema, fields, ValidationError

# json converter
#########################################
class IRSS3ContentSchema(Schema) :
    address = fields.List(fields.String, attribute = 'address')
    mime_type = fields.String(attribute = 'mime_type')
    name = fields.String(attribute = 'name')
    tags = fields.String(attribute = 'name')
    size_in_bytes = fields.String(attribute = 'size_in_bytes')
    duration_in_seconds = fields.String(attribute = 'duration_in_seconds')

class IRSS3ContextSchema(Schema) :
    type = fields.String(attribute = 'type')
    list = fields.List(fields.String, attribute = 'list')
    list_next = fields.String(attribute = 'list_next')

class IRSS3ItemSchema(Schema):
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

class IRSS3ProfileSchema(Schema) :
    name = fields.String(attribute = 'name')
    avatar = fields.String(attribute = 'avatar')
    bio = fields.String(attribute = 'bio')
    tags = fields.List(fields.String, attribute = 'tags')
    signature = fields.String(attribute = 'signature')

class IRSS3LinkSchema(Schema) :
    type = fields.String(attribute = 'type')
    tags = fields.List(fields.String, attribute = 'tags')
    list = fields.List(fields.String, attribute = 'list')
    list_next = fields.String(attribute = 'list_next')
    signature = fields.String(attribute = 'signature')

class IRSS3BacklinkSchema(Schema) :
    type = fields.String(attribute = 'type')
    list = fields.List(fields.String, attribute = 'list')
    list_next = fields.String(attribute = 'list_next')

class IRSS3AssetSchema(Schema) :
    type = fields.String(attribute = 'type')
    tags = fields.List(fields.String, attribute = 'tags')
    content = fields.String(attribute = 'content')

class IRSS3IndexSchema(Schema):
    id = fields.String(attribute = 'id')
    a_version = fields.String(attribute = '@version')
    date_created = fields.String(attribute = 'date_created')
    date_updated = fields.String(attribute = 'date_updated')
    signature = fields.String(attribute = 'signature')

    profile = fields.Nested(IRSS3ProfileSchema, attribute = 'profile')

    items = fields.Nested(IRSS3ItemSchema, attribute = 'item')
    items_next = fields.String(attribute = 'items_next')

    links = fields.List(fields.Nested(IRSS3BacklinkSchema, attribute = 'links'))
    a_backlinks = fields.List(fields.Nested(IRSS3BacklinkSchema, attribute = '@backlinks'))
    assets = fields.List(fields.Nested(IRSS3AssetSchema, attribute = 'assets'))

class IRSS3ItemsSchema(Schema) :
    id = fields.String(attribute = 'id')
    a_version = fields.String(attribute = '@version')
    date_created = fields.String(attribute = 'date_created')
    date_updated = fields.String(attribute = 'date_updated')
    signature = fields.String(attribute = 'signature')
    
    items = fields.Nested(IRSS3ItemSchema, attribute = 'item')
    items_next = fields.String(attribute = 'items_next')

class IRSS3ListSchema(Schema) :
    id = fields.String(attribute = 'id')
    
    list = fields.List(fields.String, attribute = 'list')
    next = fields.String(attribute = 'next')