from rss3_sdk.type import (
    rss3_type,
    converter
)

def get_rss3_obj(file_id, rss3_dict = None) :
    if file_id == None and (rss3_dict != None or isinstance(rss3_dict, dict)):
        raise TypeError("File_id and rss3_dict is is invalid parameter")
    if file_id.find('-items-') != -1 :
        if rss3_dict == None :
            return rss3_type.IRSS3Items(id = file_id)
        else :
            return converter.IRSS3ItemsSchema().load(rss3_dict)
    elif file_id.find('-list-') != -1 :
        if rss3_dict == None :
            return rss3_type.IRSS3List(id = file_id)
        else :
            return converter.IRSS3ListSchema().load(rss3_dict)
    else :
        if rss3_dict == None :
            return rss3_type.IRSS3Index(id = file_id)
        else :
            return converter.IRSS3IndexSchema().load(rss3_dict)

# return_type == 1 json
# return_type == 2 dict
def get_rss3_json_dict(rss3_obj, return_type = 1) :
    if rss3_obj == None and return_type == None and \
            (return_type != 1 or return_type != 2):
        raise TypeError("Rss3_obj and return_type is is invalid parameter")

    return_result = None
    if isinstance(rss3_obj, rss3_type.IRSS3Items) :
        irss3_items_schema = converter.IRSS3ItemsSchema()
        return_result = irss3_items_schema.dumps(rss3_obj) if return_type == 1 else irss3_items_schema.dump(rss3_obj)
    elif isinstance(rss3_obj, rss3_type.IRSS3List) :
        irss3_list_schema = converter.IRSS3ListSchema()
        return_result = irss3_list_schema.dumps(rss3_obj) if return_type == 1 else irss3_list_schema.dump(rss3_obj)
    elif isinstance(rss3_obj, rss3_type.IRSS3Index) :
        irss3_index_schema = converter.IRSS3IndexSchema()
        return_result = irss3_index_schema.dumps(rss3_obj) if return_type == 1 else irss3_index_schema.dump(rss3_obj)
    else :
        raise TypeError("Rss3_obj type is %s, cannot be converted to the specified type" % type(rss3_obj))

    return return_result