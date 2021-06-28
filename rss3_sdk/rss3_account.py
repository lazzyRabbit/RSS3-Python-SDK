import hexbytes
from eth_keys import keys
from eth_account import account

# If the hexadecimal number is wrong, an exception will be thrown
class RSS3Account :
    def __init__(self, private_key = None):
        self.private_key = private_key
        self.address = None
        # New account means that you can’t get it online
        self.new_account_tag = None

        if self.private_key != None :
            pk = keys.PrivateKey(hexbytes.HexBytes(self.private_key))
            self.address = pk.public_key.to_checksum_address()
            self.new_account_tag = False
        else :
            new_account_key = account.Account().create()
            self.address = new_account_key.address
            self.private_key = hexbytes.HexBytes(new_account_key.key).hex()
            self.new_account_tag = True
