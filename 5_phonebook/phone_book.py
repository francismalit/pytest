dir_path = "D:\\userdata\\malit\\Desktop\\class_room\\python\\5_phonebook\\"


def add(name, contact):
    pbook = open("test_phone_book.txt")
    pbook.write(name + ", " + contact)
    return True


def save(fileName):
    pbook = open(dir_path + fileName, 'wb')
    pbook.write("hello world")
    return True


def count(fileName):

    pbook = open(dir_path + fileName, 'wb')
