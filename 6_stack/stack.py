from abc import abstractmethod


class Stack:

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
