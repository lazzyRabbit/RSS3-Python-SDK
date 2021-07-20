from rss3_sdk.module.base import account
from rss3_sdk.module.rss3 import base,index

import logging
logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(lineno)s - %(message)s')
logger = logging.getLogger(__name__)

if __name__ == '__main__':
    rss3_option = base.ModuleOption(
        account = account.Account('0xa55afab0f35bdc00c1ac137a98d5d037609eeaead8ba930c4c3878e38630e38a'),
        endpoint='hub.rss3.io',
    )
    rss3_index = index.RSS3(rss3_option)

    inn_item = rss3_index.item.get("0x13e1ED9aec15Bf75AD081fB5E5466701F4E9bF4B-item-3")
    logger.info(inn_item.__dict__)
    inn_item.summary = inn_item.summary + "3"

    inn_profile = rss3_index.profile.get()
    logger.info(inn_profile.__dict__)
    inn_profile.name = "fuck the world3"

    rss3_index.file.update()

