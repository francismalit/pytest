from collections import OrderedDict


class ClassParser(object):

    def __init__(self, string):
        string = string.replace("\n", "").replace("  ", "")
        end = string.find("(")
        self.__name = string[6: end]
        self.__method = OrderedDict()
        string = string[end: -1]
        while -1 != string.find("def"):
            # start of parsing key
            start = string.find("def")
            string = string[start: -1]
            end = string.find("(")
            _key = string[4: end]
            string = string[end + 7: -1]
            # start of parsing value
            end = string.find("def")
            _value = string[0: end]
            self.__method[_key] = _value
            string = string[end: - 1]
            if -1 == string.find("def"):
                break



    # def __init__(self, string):
    #     split_string = string.split("\nclass ")[1].split("(object)")
    #     self.__name = split_string[0]
    #     self.__method = {}
    #     split_string = split_string[1]
    #     while split_string.find("def"):
    #         functionStart = split_string.find("def")
    #         split_string = split_string[functionStart + 4: -1]
    #         end_funct = split_string.find("(self")
    #         # self.__method.append(split_string[0:end_funct])
    #
    #         _key = split_string[0:end_funct]
    #         _value = split_string[end_funct: -1]
    #         split_string = split_string[end_funct: -1].replace("\n", "", 1).strip()
    #         # .replace("\n", "", 1)
    #         self.__method.update({_key, _value})
    #         split_string = split_string[end_funct: -1]
    #         if -1 == split_string.find("def"):
    #             break

    @property
    def name(self):
        return self.__name

    @property
    def methods(self):
        return self.__method.keys()

    @property
    def init(self):
        return "Property does not exist"


    def __getitem__(self, item):
        return item