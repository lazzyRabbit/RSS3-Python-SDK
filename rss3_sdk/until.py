import json
import copy
import hexbytes
from _pysha3 import keccak_256
from type import rss_type
from datetime import datetime
from eth_keys import keys, datatypes
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
    new_data = copy.deepcopy(data) # 深拷贝一组
    for key in new_data :
        if key.firsts[0] == '@' or key == 'signature' :
            del data[key]
    return new_data

# Since I don’t know the specific type of irss3,
# it needs to be converted into a dict outside the function
# sign(irss3_dict, private_key) and check(irss3_dict, personal)
# Of course, sign_msg has an automatic hash converted to keccak256 inside

def sign(irss3_data, private_key) :
    if irss3_data == None or private_key == None :
        return None
    irss3_json_msg = json.dumps(remove_not_sign_properties(irss3_data))
    return private_key.sign_msg(irss3_json_msg).to_hex()

def check(irss3_data, personal_address) :
    if irss3_data == None or irss3_data.signature == None or personal_address == None:
        return False
    else :
        irss3_json_msg = json.dumps(remove_not_sign_properties(irss3_data))
        curr_eth_sign = datatypes.Signature(hexbytes.HexBytes(irss3_data.signature))
        curr_address = curr_eth_sign.recover_public_key_from_msg(irss3_json_msg)
        print("curr_address: %s" % curr_address)
        return curr_address == personal_address

def get_rss3_obj(file_id) :
    if file_id == None :
        return None
    if file_id.find('-items-') != -1 :
        return rss_type.IRSS3Items(id = file_id)
    elif file_id.find('-list-') != -1 :
        return rss_type.IRSS3List(id = file_id)
    else :
        return rss_type.IRSS3Index(id = file_id)

def get_rss3_json(rss3_obj):
    if rss3_obj == None :
        return None
    if rss3_obj.id.find('-items-') != -1 :
        irss3_items_schema = converter.IRSS3ItemsSchema()
        return irss3_items_schema.dumps(rss3_obj)
    elif rss3_obj.find('-list-') != -1 :
        irss3_list_schema = converter.IRSS3ListSchema()
        irss3_list_schema.dumps(rss3_obj)
    else :  #index
        irss3_index_schema = converter.IRSS3IndexSchema()
        return irss3_index_schema.dumps(rss3_obj)

