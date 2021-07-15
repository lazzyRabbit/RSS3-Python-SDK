from . import (
    base
)

class Personal(base.BaseModule):
    def __init__(self, option):
        base.BaseModule.__init__(self, option)
        pass

    def get(self):
        return None

    def patch(self):
        return None