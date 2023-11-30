#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    if len(argv) == 1:
        print("0 arguments.")
    elif len(argv) == 2:
        print("1 argument:")
        print("{:d}: {}".format(len(argv) - 1, argv[1]))
    elif len(argv) > 2:
        print("{:d} arguments:".format(len(argv) - 1))
        for i in range(1, len(argv)):
            print("{:d}: {}".format(i, argv[i]))
