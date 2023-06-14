#!/usr/bin/python3
"""Script to read stdin line by line and computes metrics"""
import sys


class Stats:
    """Defines a Stats class to print stats info"""

    def __init__(self):
        """Initialize the dict that will hold informations
           and the size
        """
        self.dic = {}
        self.size = 0

    def init_info(self):
        """init info in the dic"""
        self.dic["200"] = 0
        self.dic["301"] = 0
        self.dic["400"] = 0
        self.dic["401"] = 0
        self.dic["403"] = 0
        self.dic["404"] = 0
        self.dic["405"] = 0
        self.dic["500"] = 0

    def inc_status(self, status):
        """Increment the number of status code"""
        if status in self.dic:
            self.dic[status] += 1

    def print_info(self):
        """Print info"""
        print("File size: {}".format(self.size))
        for key in sorted(self.dic.keys()):
            if self.dic[key] != 0:
                print("{}: {:d}".format(key, self.dic[key]))


if __name__ == "__main__":
    stat = Stats()
    stat.init_info()
    count = 0

    try:
        for line in sys.stdin:
            if count != 0 and count % 10 == 0:
                stat.print_info()

            try:
                word_line = [x for x in line.split(" ")]
                stat.inc_status(word_line[-2])
                stat.size += int(word_line[-1].strip("\n"))
            except Exception:
                pass

            count += 1
    except KeyboardInterrupt:
        stat.print_info()
        raise
