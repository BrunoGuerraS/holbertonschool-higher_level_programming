#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    res = 0
    for a in range(1, len(sys.argv)):
        res += int(sys.argv[a])
    print("{}".format(res))
