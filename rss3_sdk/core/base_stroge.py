import abc

class BaseStroge(metaclass = abc.ABCMeta):
    @abc.abstractmethod
    def save_file(self, id, file):
        return None

    @abc.abstractmethod
    def get_file(self, id):
        return None