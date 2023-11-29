#!/usr/bin/python3
def islower(c):
    if ord(c) in range(97, 123):
        return True
    else:
        return False


def uppercase(str):
    upp_str = ""
    for c in str:
        if islower(c):
            upp_str += chr(ord(c) - 32)
        else:
            upp_str += c

    print("{}".format(upp_str))
