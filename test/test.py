import hexbytes
from eth_keys import keys, datatypes
from eth_utils import hexadecimal
from web3.auto import w3
from rss3_sdk import rss3_account
from rss3_sdk import rss3_handle
import urllib3
from rss3_sdk import until
import json

if __name__ == '__main__':

    # message_hash = '0x1476abb745d423bf09273f1afd887d951181d25adc66c4834a70491911b7f750'
    # signature = '0xe6ca9bba58c88611fad66a6ce8f996908195593807c4b38bd528d2cff09d4eb33e5bfbbf4d3e39b1a2fd816a7680c19ebebaf3a141b239934ad43cb33fcec8ce1c'
    # w3.eth.account.recoverHash(message_hash, signature=signature)

    # msg = "I♥SF"
    # private_key = b"\xb2\\}\xb3\x1f\xee\xd9\x12''\xbf\t9\xdcv\x9a\x96VK-\xe4\xc4rm\x03[6\xec\xf1\xe5\xb3d"
    # message = encode_defunct(text=msg)


    # curr_account = rss3_account.RSS3Account('0xa55afab0f35bdc00c1ac137a98d5d037609eeaead8ba930c4c3878e38630e38a')

    # curr_account = rss3_account.RSS3Account('0x47e18d6c386898b424025cd9db446f779ef24ad33a26c499c87bb3d9372540ba')
    # handle = rss3_handle.RSS3Handle(
    #     endpoint='rss3-hub-playground-6raed.ondigitalocean.app',
    #     rss3_account=curr_account)

    # '''
    curr_account = rss3_account.RSS3Account('0xa55afab0f35bdc00c1ac137a98d5d037609eeaead8ba930c4c3878e38630e38a')
    handle = rss3_handle.RSS3Handle(
        endpoint='hub.rss3.io',
        rss3_account=curr_account)

    inn_profile = handle.profile_get()
    print(inn_profile)
    inn_profile.name = "fuck the world"
    handle.profile_patch(inn_profile)
    handle.update_file()
    # '''

    print(until.get_datetime_isostring())

    # proxy = urllib3.ProxyManager("http://127.0.0.1:4780/")
    # resp1 = proxy.request("GET", "https://www.google.com/")

    ###############################

    # 帮助测试一下
    '''
    test_dict = {
      "authors": [
        "0x6338ee94fB85e157D117d681E808a34a9aC21f31"
      ],
      "title": "Hello",
      "id": "0x6338ee94fB85e157D117d681E808a34a9aC21f31-item-7",
      "date_published": "2021-05-22T12:52:27.489Z",
      "date_modified": "2021-05-22T12:52:27.489Z",
      "signature": "0xc50406cf36be5fd1d4e414e616f7257a2c401defc15b939748ce5ae7d957b7a355519baf6db50d8390962c889f15c51a57710dabdade044b2482da7024be6e841c"
    }
    '''

    # test_dict = json.loads(test_json)

    # test_dict = until.remove_empty_properties(test_dict)
    # signature = until.sign(test_dict, '47e18d6c386898b424025cd9db446f779ef24ad33a26c499c87bb3d9372540ba')
    # print(signature)

    # curr_account = rss3_account.RSS3Account('47e18d6c386898b424025cd9db446f779ef24ad33a26c499c87bb3d9372540ba')
    # print(curr_account.address)
    # print(until.check(test_dict, curr_account.address))

    ###############################

    '''
    test_dict = {
        "authors": [
            "0x13e1ED9aec15Bf75AD081fB5E5466701F4E9bF4B"
        ],
        "summary": "hello rss3",
        "tags": [
            "Re: ID",
            "Twitter"
        ],
        "id": "0x13e1ED9aec15Bf75AD081fB5E5466701F4E9bF4B-item-0",
        "date_published": "2021-07-04T09:29:17.761Z",
        "date_modified": "2021-07-04T09:29:17.761Z",
        "signature": "0x38b59e88c9d95d32bb38da812437659a5959b6cefc3794c4348d4660fec49b0a404133f9ff8cd515e8c9af375e0f9d2ab506697d5c398ce807c1df342799be221c"
    }

    test_dict = until.remove_empty_properties(test_dict)
    signature = until.sign(test_dict, '0xa55afab0f35bdc00c1ac137a98d5d037609eeaead8ba930c4c3878e38630e38a')
    print(signature)
    '''