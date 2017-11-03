def length(string):
    return len(string)


def without(string1, string2):
    output = string1
    for s in string2:
        output = output.replace(s, "", -1)
    return output


def count_distinct(string):
    return set(string).__len__()


def tokens(string):
    l = set(string.split("."))
    if "" in l:
      l.remove("")
    toList = list(l)
    return toList




