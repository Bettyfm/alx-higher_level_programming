#!/usr/bin/python3
def print_last_digit(number):
    last_dig = number % 10 if number >= 0 else number % -10
    print("{}".format(number % 10))
    return last_dig
