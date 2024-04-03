def read_file_list(filename):
    with open(filename, 'r') as file:
        return file.readlines()

    # hint: when you read lines of files, there will be a "newline"
    # (end-of-line character) at the end of each line, and you want to
    # strip that off before you print it. Do some research on that!