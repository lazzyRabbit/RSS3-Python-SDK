from rss3_sdk.module.rss3 import (
    file as rss3_file,
    items as rss3_items,
    profile as rss_profile,
    item as rss3_item
)

class RSS3():
    def __init__(self, option):
        self.file = rss3_file.File(option)
        option.rss3_stroge = self.file

        self.item = rss3_item.Item(option)
        self.items = rss3_items.Items(option)
        self.profile = rss_profile.Profile(option)

