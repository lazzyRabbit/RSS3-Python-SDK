import json
import copy
import hexbytes
from _pysha3 import keccak_256
from .type import rss3_type
from datetime import datetime
from eth_keys import keys, datatypes
from eth_keys.utils.address import public_key_bytes_to_address
from . import converter

def get_datetime_isostring() :
    dt = datetime.now()
    try:
        utc = dt + dt.utcoffset()
    except TypeError as e:
        utc = dt
    isostring = datetime.strftime(utc, '%Y-%m-%dT%H:%M:%S.{0}Z')
    return isostring.format(int(round(utc.microsecond/1000.0)))

def remove_not_sign_properties(data) :
    new_data = copy.deepcopy(data)
    for key in data :
        if ('a_' in key) or key == 'signature' :
            del new_data[key]
    return new_data

def value_is_not_empty(value):
    return value not in ['', None, {}, []]

def remove_empty_properties(data) :
    if isinstance(data, dict):
        temp_data = dict()
        for key, value in data.items():
            if value_is_not_empty(value):
                new_value = remove_empty_properties(value)
                if value_is_not_empty(new_value):
                    temp_data[key] = new_value
        return None if not temp_data else temp_data

    elif isinstance(data, list):
        temp_data = list()
        for value in data:
            if value_is_not_empty(value):
                new_value = remove_empty_properties(value)
                if value_is_not_empty(new_value):
                    temp_data.append(new_value)
        return None if not temp_data else temp_data

    elif value_is_not_empty(data):
        return data

# Since I don’t know the specific type of irss3,
# it needs to be converted into a dict outside the function
# sign(irss3_dict, private_key) and check(irss3_dict, personal)
# Of course, sign_msg has an automatic hash converted to keccak256 inside

def sign(irss3_data, private_key) :
    if irss3_data == None or private_key == None :
        return None
    irss3_json_msg = json.dumps(remove_not_sign_properties(irss3_data))
    eth_private_key = keys.PrivateKey(hexbytes.HexBytes(private_key))
    bytes_irss3_json_msg = bytes(irss3_json_msg, 'utf-8')

    return eth_private_key.sign_msg(bytes_irss3_json_msg).to_hex()

def check(irss3_data, personal_address) :
    if irss3_data == None or type(irss3_data) != dict or irss3_data['signature'] == None or personal_address == None :
        return False

    irss3_json_msg = json.dumps(remove_not_sign_properties(irss3_data))
    curr_eth_sign = datatypes.Signature(hexbytes.HexBytes(irss3_data['signature']))
    public_key = curr_eth_sign.recover_public_key_from_msg(irss3_json_msg) # 这里需要转换一下
    curr_address = public_key_bytes_to_address(hexbytes.HexBytes(public_key))
    return curr_address == personal_address

def get_rss3_obj(file_id) :
    if file_id == None :
        raise TypeError("File_id is null")
    if file_id.find('-items-') != -1 :
        return rss3_type.IRSS3Items(id = file_id)
    elif file_id.find('-list-') != -1 :
        return rss3_type.IRSS3List(id = file_id)
    else :
        return rss3_type.IRSS3Index(id = file_id)

# return_type == 1 json
# return_type == 2 dict
def get_rss3_json_dict(rss3_obj, return_type = 1):
    if rss3_obj == None and return_type == None and \
            (return_type != 1 or return_type != 2):
        raise TypeError("Rss3_obj and return_type is is invalid parameter")

    return_result = None
    if type(rss3_obj) == rss3_type.IRSS3Items:
        irss3_items_schema = converter.IRSS3ItemsSchema()
        return_result = irss3_items_schema.dumps(rss3_obj) if return_type == 1 else irss3_items_schema.dump(rss3_obj)
    elif type(rss3_obj) == rss3_type.IRSS3List:
        irss3_list_schema = converter.IRSS3ListSchema()
        return_result = irss3_list_schema.dumps(rss3_obj) if return_type == 1 else irss3_list_schema.dump(rss3_obj)
    elif type(rss3_obj) == rss3_type.IRSS3Index:
        irss3_index_schema = converter.IRSS3IndexSchema()
        return_result = irss3_index_schema.dumps(rss3_obj) if return_type == 1 else irss3_index_schema.dump(rss3_obj)
    else :
        raise TypeError("Rss3_obj type is %s, cannot be converted to the specified type" % type(rss3_obj))

    return return_result



