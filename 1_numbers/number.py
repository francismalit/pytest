def add(*num):
    sum = 0
    for number in num:
        sum += number
    return sum


def multiply(*num):
    product = 1
    for number in num:
        product *= number
    return product


def divide(num1, num2):
    if 0 == num1 or 0 == num2:
        return 0
    else:
        return num1 / num2


def add_two_largest(*num):
    numbers = sorted(num, reverse=True)[0:2]
    return numbers[0] + numbers[1]
