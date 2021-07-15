from . import (
    data_handle
)

from web3.auto import (
    w3
)

from eth_account.messages import (
    encode_defunct
)

def sign(irss3_data, private_key) :
    if irss3_data == None or private_key == None :
        return None

    irss3_json_msg = data_handle.irss3_data_dump_handle(irss3_data)
    message = encode_defunct(text = irss3_json_msg)

    return w3.eth.account.sign_message(message, private_key).signature.hex()

def check(irss3_data, personal_address) :
    if irss3_data == None or isinstance(irss3_data, dict) == False or irss3_data['signature'] == None or personal_address == None :
        return False

    irss3_json_msg = data_handle.rss3_data_dump_handle(irss3_data)
    message = encode_defunct(text = irss3_json_msg)
    return w3.eth.account.recover_message(message, signature=irss3_data['signature']) == personal_address