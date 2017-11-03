def sort(*num):
    return sorted(num)


def maximum(*num):
    return sorted(num, reverse=True)[:1]


def positives(*num):
    list = []
    for number in num:
        if number >= 0:
            list += [number]
    return list
