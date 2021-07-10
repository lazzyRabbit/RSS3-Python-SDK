import abc

class RSS3Module :
    @abc.abstractmethod
    def get(self):
        pass

    @abc.abstractmethod
    def patch(self):
        pass