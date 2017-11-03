# from abc import ABCMeta
import abc
from abc import abstractmethod


class Stack:
    __metaclass__ = abc.ABCMeta

    # @property
    # def prop(self):
    #     pass

    def __init__(self):
        self.__stack = []

    def get_size(self):
        return len(self.__stack)

    def push(self, obj):
        self.__stack.append(obj)

    def pop(self):
        if self.get_size() > 0:
            self.__stack.pop()
        else:
            return None

    @abstractmethod
    def area(self):
        pass


# from datetime import datetime, timedelta