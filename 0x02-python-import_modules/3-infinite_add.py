#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    sum = 0
    n = len(argv)
    for i in range(1, n):
        sum += int(argv[i])

    print(sum)
