#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, 'r') as file:
        file_read = file.read()
    print(file_read)
