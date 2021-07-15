from rss3_sdk.until2 import (
    account as rss3_account
)

class ModuleOption:
    def __init__(self, account, endpoint='hub.rss3.io'):
        self._endpoint = endpoint
        self._account = account
        if self._account == None or isinstance(account, rss3_account.RSS3Account) == False:
            raise ValueError("Account is invalid parameter")


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