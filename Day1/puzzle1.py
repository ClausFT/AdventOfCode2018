#!/usr/bin/python

def main():
    file = open("input.txt", "r")
    frequency = 0
    for line in file.readlines():
        frequency += int(line.strip())
    print(frequency)

if __name__ == '__main__':
    main()