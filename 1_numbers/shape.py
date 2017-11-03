import abc


class Shape:

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_area(self):
        pass
