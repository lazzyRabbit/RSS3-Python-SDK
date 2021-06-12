import sys
import sha3
import hexbytes
from rss3_sdk import rss3_handle
from rss3_sdk import until
from eth_keys import keys, datatypes
from eth_account import account

def fill_update_new_callback() :
    print("this is call back")

if __name__ == '__main__':
    # item = rss_type.IRSS3Item()
    # item.title = "sada"
    # print(item.title)

    # index.test_main.test()

    # test for interface

    '''
    option = rss3_opr.RSS3Option(endpoint = 'https://rss3-hub-playground-6raed.ondigitalocean.app/',
                                 private_key = '0x47e18d6c386898b424025cd9db446f779ef24ad33a26c499c87bb3d9372540ba',
                                 fill_update_callback = fill_update_new_callback)

    rss3_handle = rss3_opr.RSS3Handle(option)
    file_id = '0x6338ee94fB85e157D117d681E808a34a9aC21f31'
    # 0x47e18d6c386898b424025cd9db446f779ef24ad33a26c499c87bb3d9372540ba
    # 0xc50406cf36be5fd1d4e414e616f7257a2c401defc15b939748ce5ae7d957b7a355519baf6db50d8390962c889f15c51a57710dabdade044b2482da7024be6e841c
    if rss3_handle.init() == False :
        print("you are SB")
        exit(-1)
    # rss3_handle.getFile(file_id)

    # test
    # rss3_inner_stroge = rss3_handle.get_inner_stroge()
    # rss3_inner_stroge.getFile()

    # print (test_dict)
    '''

    # print("until: %s" % until.get_datetime_isostring())

    # 生成count test
    # curr_account = account.Account()
    keyss = account.Account().create()
    print(keyss.address)
    print(type(keyss.address))
    pk = hexbytes.HexBytes(keyss.key).hex()
    print(pk)
    print(type(pk))

    pk2 = keys.PrivateKey(hexbytes.HexBytes(pk))
    private_key = pk2.public_key.to_checksum_address()
    print(pk2)
    print(private_key)

    # 公私钥test
    '''
    pk = '0x47e18d6c386898b424025cd9db446f779ef24ad33a26c499c87bb3d9372540ba'
    pk = keys.PrivateKey(hexbytes.HexBytes(pk))
    private_key = pk.public_key.to_checksum_address()
    print(private_key)
    print(type(private_key))
    signature = pk.sign_msg(b'a message')
    print(signature)
    print(signature.to_hex())
    print(type(signature))
    print(type(signature.to_hex()))

    # b_signature = bytes(signature.to_hex(), encoding='utf-8')
    curr_eth_sign = datatypes.Signature(hexbytes.HexBytes(signature.to_hex()))
    print(curr_eth_sign)
    '''
