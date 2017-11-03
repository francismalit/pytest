def read(textFile):

    output = ""
    print output
    try:
        inputFile = open(textFile)
        output = inputFile.read()
    finally:
        inputFile.close()
    return output


def contains(string, textFile):

    fileContent = read(textFile)
    return fileContent.find(string) != -1


def file_rows_startingwith(string, textFile):

    output = ""
    print output
    try:
        inputFile = open(textFile)
        lines = inputFile.readlines() #refactor
    finally:
        inputFile.close()

    for line in lines:
        if line.startswith(string):
            output += line

    return output