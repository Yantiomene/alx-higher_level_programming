#!/usr/bin/python3
for i in range(9):
    for j in range(1, 10):
        if i < j:
            if i == 8 and j == 9:
                print("{:d}{:d}".format(i, j))
                break
            print("{:d}{:d}".format(i, j), end=", ")
