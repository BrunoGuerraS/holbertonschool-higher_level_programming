#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print("0 arguments.")
    elif len(sys.argv) == 2:
        print("{} argument:".format(len(sys.argv) - 1))
        for a in range(1, len(sys.argv)):
            print("{}: {}".format(a, sys.argv[a]))
    else:
        print("{} arguments:".format(len(sys.argv) - 1))
        for a in range(1, len(sys.argv)):
            print("{}: {}".format(a, sys.argv[a]))
