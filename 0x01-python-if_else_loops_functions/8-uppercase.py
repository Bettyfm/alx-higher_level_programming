#!/usr/bin/python3
def islower(c):
    if ord(c) in range(97, 123):
        return True
    else:
        return False


def uppercase(str):
    for c in str:
        C = c
        if islower(c):
            C = chr(ord(c) - 32)
            print("{}".format(C), end=" ")
    print("")
