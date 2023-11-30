#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    length = len(argv)
    count = 0
    for i in range(1, length):
        count += int(argv[i])
    print("{:d}".format(count))
