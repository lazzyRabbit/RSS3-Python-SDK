from . import (
    base
)

from rss3_sdk.type import (
    inn_type,
    rss3_type
)

from rss3_sdk.until2 import (
    time
)

class File(base.BaseModule):
    def __init__(self):
        self._file_stroge_dict = {}
        self._file_update_tag = set()
        pass

    def get(self):
        return None

    # Most patches are used more
    def update(self, rss3_base):
        if isinstance(rss3_base, rss3_type.IRSS3Base) == False:
            raise ("Rss3_base type is error")

        rss3_base.date_updated = time.get_datetime_isostring()
        self._file_stroge_dict[rss3_base.id] = rss3_base
        self._file_update_tag.add(self._rss3_account.address)

    def _get_file_from_net(self):
        pass
