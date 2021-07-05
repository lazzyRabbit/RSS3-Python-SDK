import json
import copy
from .type import rss3_type
from datetime import datetime
from . import converter
from web3.auto import w3
from eth_account.messages import encode_defunct

import logging
logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(lineno)s - %(message)s')
logger = logging.getLogger(__name__)

def get_datetime_isostring() :
    dt = datetime.now()
    try:
        utc = dt + dt.utcoffset()
    except TypeError as e:
        utc = dt
    isostring = datetime.strftime(utc, '%Y-%m-%dT%H:%M:%S.{0}Z')
    return isostring.format(int(round(utc.microsecond/1000.0)))

#########################################

def value_is_not_empty(value) :
    return value not in ['', None, {}, []]

def remove_not_sign_properties(data) :
    temp_data = dict()
    for key, value in data.items():
        if (key.find('@') == -1) and key != 'signature' :
            temp_data[key] = value
    return temp_data

def remove_empty_properties(data) :
    if isinstance(data, dict):
        temp_data = dict()
        for key, value in data.items():
            if value_is_not_empty(value):
                new_value = remove_empty_properties(value)
                if value_is_not_empty(new_value) :
                    temp_data[key] = new_value
        return None if not temp_data else temp_data

    elif isinstance(data, list):
        temp_data = list()
        for value in data:
            if value_is_not_empty(value):
                new_value = remove_empty_properties(value)
                if value_is_not_empty(new_value) :
                    temp_data.append(new_value)
        return None if not temp_data else temp_data

    elif value_is_not_empty(data):
        return data

def sorted_irss_dict(data) :
    if isinstance(data, dict) :
        temp_data = dict()
        for key, value in data.items() :
            new_value = sorted_irss_dict(value)
            temp_data[key] = new_value
        return sorted(temp_data.items(), key=lambda d: d[0])

    elif isinstance(data, list) :
        temp_data = list()
        count = 0
        for value in data:
            new_value = sorted_irss_dict(value)
            temp_data.append([str(count), new_value])
            count = count + 1
        logger.info("temp_data : %s" % temp_data)
        return None if not temp_data else temp_data

    elif value_is_not_empty(data) :
        return data

def irss3_data_dump_handle(irss3_data) :
    not_sign_irss3_data = copy.deepcopy(irss3_data)
    not_sign_irss3_data = remove_not_sign_properties(not_sign_irss3_data)
    not_sign_irss3_data = sorted_irss_dict(not_sign_irss3_data)

    return json.dumps(not_sign_irss3_data, separators=(',',':'))

#########################################

def sign(irss3_data, private_key) :
    if irss3_data == None or private_key == None :
        return None
    not_sign_irss3_data = copy.deepcopy(irss3_data)
    logger.info(not_sign_irss3_data)
    irss3_json_msg = irss3_data_dump_handle(irss3_data_dump_handle(irss3_data))

    return w3.eth.account.sign_message(irss3_json_msg, private_key).signature

def check(irss3_data, personal_address) :
    if irss3_data == None or isinstance(irss3_data, dict) == False or irss3_data['signature'] == None or personal_address == None :
        return False

    # not_sign_irss3_data = copy.deepcopy(irss3_data)
    # not_sign_irss3_data = remove_not_sign_properties(not_sign_irss3_data)
    # not_sign_irss3_data = sorted_irss_dict(not_sign_irss3_data)
    irss3_json_msg = irss3_data_dump_handle(irss3_data)
    logger.info(irss3_json_msg)
    message = encode_defunct(text = irss3_json_msg)
    logger.info(irss3_data['signature'])
    # logger.info(irss3_data['signature'])
    ddd = w3.eth.account.recover_message(message, signature = irss3_data['signature'])
    logger.info(ddd)
    # logger.info(type(personal_address), personal_address)
    return w3.eth.account.recover_message(message, signature=irss3_data['signature']) == personal_address


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
    if isinstance(rss3_obj, rss3_type.IRSS3Items):
        irss3_items_schema = converter.IRSS3ItemsSchema()
        return_result = irss3_items_schema.dumps(rss3_obj) if return_type == 1 else irss3_items_schema.dump(rss3_obj)
    elif isinstance(rss3_obj, rss3_type.IRSS3List):
        irss3_list_schema = converter.IRSS3ListSchema()
        return_result = irss3_list_schema.dumps(rss3_obj) if return_type == 1 else irss3_list_schema.dump(rss3_obj)
    elif isinstance(rss3_obj, rss3_type.IRSS3Index):
        irss3_index_schema = converter.IRSS3IndexSchema()
        return_result = irss3_index_schema.dumps(rss3_obj) if return_type == 1 else irss3_index_schema.dump(rss3_obj)
    else :
        raise TypeError("Rss3_obj type is %s, cannot be converted to the specified type" % type(rss3_obj))

    return return_result



