from rss3_sdk.until2 import (
    account as rss3_account
)

from rss3_sdk.core import (
    local_stroge as stroge
)

class ModuleOption:
    def __init__(self,
                 account,
                 file_stroge=stroge.LocalStroge(),
                 endpoint='hub.rss3.io'):

        if account == None or isinstance(account, rss3_account.Account) == False\
        or file_stroge == None or isinstance(file_stroge, stroge.LocalStroge) == False\
        or endpoint == None or isinstance(endpoint, str):
            raise ValueError("Invalid parameter")

        self.account = account
        self.file_stroge = file_stroge
        self.endpoint = endpoint

class BaseModule:
    def __init__(self, option):
        if option == None or isinstance(option, ModuleOption) == False:
            raise ValueError("Option is invalid parameter")
        self._option = option
        pass

    def get(self):
        return None

    def patch(self):
        return None