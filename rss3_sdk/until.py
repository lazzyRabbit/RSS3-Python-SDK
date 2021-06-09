import json
import copy
import hexbytes
from _pysha3 import keccak_256
from type import rss_type
from datetime import datetime
from eth_keys import keys, datatypes

def get_datetime_isostring() :
    dt = datetime.now()
    try:
        utc = dt + dt.utcoffset()
    except TypeError as e:
        utc = dt
    isostring = datetime.strftime(utc, '%Y-%m-%dT%H:%M:%S.{0}Z')
    return isostring.format(int(round(utc.microsecond/1000.0)))

def removeNotSignProperties(data) :
    new_data = copy.deepcopy(data) # 深拷贝一组
    for key in new_data :
        if key.firsts[0] == '@' or key == 'signature' :
            del data[key]
    return new_data

# Since I don’t know the specific type of irss3,
# it needs to be converted into a dict outside the function
# sign(irss3_dict, private_key) and check(irss3_dict, personal)
# Of course, sign_msg has an automatic hash converted to keccak256 inside

def sign(irss3_dict, private_key) :
    if irss3_dict == None or private_key == None :
        return None
    irss3_json_msg = json.dumps(removeNotSignProperties(irss3_dict))
    return private_key.sign_msg(irss3_json_msg).to_hex()

def check(irss3_dict, personal_address) :
    if irss3_dict == None or irss3_dict.signature == None or personal_address == None:
        return False
    else :
        irss3_json_msg = json.dumps(removeNotSignProperties(irss3_dict))
        curr_eth_sign = datatypes.Signature(hexbytes.HexBytes(irss3_dict.signature))
        curr_address = curr_eth_sign.recover_public_key_from_msg(irss3_json_msg)
        print("curr_address: %s" % curr_address)
        return curr_address == personal_address