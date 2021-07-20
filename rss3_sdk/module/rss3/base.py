import urllib3

from rss3_sdk.module.base import (
    account as rss3_account,
    base_stroge,
    local_stroge
)

from rss3_sdk import (
    config
)

from rss3_sdk.until import (
    time
)

from rss3_sdk.type import (
    rss3_type
)

import logging
logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(lineno)s - %(message)s')
logger = logging.getLogger(__name__)

class ModuleOption:
    def __init__(self,
                 account,
                 file_stroge = local_stroge.LocalStroge(),
                 endpoint = 'hub.rss3.io'):

        if account == None or isinstance(account, rss3_account.Account) == False\
        or file_stroge == None or isinstance(file_stroge, base_stroge.BaseStroge) == False\
        or endpoint == None or isinstance(endpoint, str) == False:
            raise ValueError("Invalid parameter")

        self.account = account
        self.file_stroge = file_stroge
        self.endpoint = endpoint

        if 'proxy' in config.conf :
            self.http = urllib3.ProxyManager(config.conf['proxy'])
        else :
            self.http = urllib3.PoolManager()

        # file_stroge is precisely the caching layer, which is the real resource acquisition layer
        self.rss3_stroge = None
        # Update cache used to record the current rss operation
        self.file_update_tag = set()

class BaseModule:
    def __init__(self, option):
        if option == None or isinstance(option, ModuleOption) == False:
            raise ValueError("Option is invalid parameter")
        self._option = option

    def get(self):
        return None

    def patch(self, inn_data):
        return None

    def post(self, inn_data):
        return None

    def update(self):
        return None

    def _update_file_stroge(self, irss3_base):
        if isinstance(irss3_base, rss3_type.IRSS3Base) == False:
            raise ValueError("irss3_base is invalid parameter")

        time_now = time.get_datetime_isostring()
        if irss3_base.date_created == None:
            irss3_base.date_created = time_now
        irss3_base.date_updated = time_now
        self._option.update_file(irss3_base.id, irss3_base)
        self._file_update_tag.add(irss3_base.id)

