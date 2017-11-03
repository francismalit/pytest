class SUT(object):

    @staticmethod
    def method(self, _string):
        string_length = len(_string)
        if string_length < 5:
            return "short text"
        elif string_length:
            return "long text"
