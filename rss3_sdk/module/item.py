from . import (
    base
)

class Item(base.BaseModule):
    def __init__(self, option):
        base.BaseModule.__init__(self, option)
        pass

    def get(self):
        return None

    def patch(self):
        return None

    def post(self):
        return None