#!/usr/bin/python
from itertools import cycle

def main():
    file = open("input.txt", "r")
    valuePool = cycle([int(i.strip()) for i in file.readlines()])
    frequencies = set()
    frequency = 0
    for value in valuePool:
        frequency += value
        if (frequency in frequencies):
            print (frequency)
            break
        frequencies.add(frequency)
        
if __name__ == '__main__':
    main()