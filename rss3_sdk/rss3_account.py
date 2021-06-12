import hexbytes
from eth_keys import keys
from eth_account import account

class RSS3Account :
    def __init__(self, private_key = None):
        self.private_key = private_key
        self.address = None
        # 新账户，意味着去网上拉不到
        self.new_account_tag = None

        if self.private_key != None :
            pk = keys.PrivateKey(hexbytes.HexBytes(self.__option.private_key))
            # 这里要到时候检查一下不是16位会不会抛出异常
            self.address = pk.public_key.to_checksum_address()
            self.new_account_tag = False
        else :
            new_account_key = account.Account().create()
            self.address = new_account_key.address
            self.private_key = hexbytes.HexBytes(new_account_key.key).hex()
            self.new_account_tag = True
