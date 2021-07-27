from rss3_sdk.module.rss3 import (
    base as rss3_base
)

class Items(rss3_base.BaseModule):
    def __init__(self, option):
        super().__init__(option)

    def get(self):
        pass
