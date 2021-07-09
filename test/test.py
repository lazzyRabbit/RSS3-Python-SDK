import hexbytes
from eth_keys import keys, datatypes
from eth_utils import hexadecimal
from web3.auto import w3
from rss3_sdk import rss3_account
from rss3_sdk import rss3_handle
import urllib3

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

    curr_account = rss3_account.RSS3Account('0xa55afab0f35bdc00c1ac137a98d5d037609eeaead8ba930c4c3878e38630e38a')
    handle = rss3_handle.RSS3Handle(
        endpoint='hub.rss3.io',
        rss3_account=curr_account)

    inn_profile = handle.profile_get()
    print(inn_profile)
    inn_profile.name = "fuck the world"
    handle.profile_patch(inn_profile)
    handle.update_file()


    # proxy = urllib3.ProxyManager("http://127.0.0.1:4780/")
    # resp1 = proxy.request("GET", "https://www.google.com/")