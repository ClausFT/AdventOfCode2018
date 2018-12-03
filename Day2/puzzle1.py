#!/usr/bin/python

def main():
    file = open("input.txt", "r")
    twoLetterCount = 0
    threeLetterCount = 0
    for line in file.readlines():
        twoLetterMatch = False
        threeLetterMatch = False
        for char in line:
            twoLetterMatch = True if line.count(char) == 2 else twoLetterMatch
            threeLetterMatch = True if line.count(char) == 3 else threeLetterMatch
                
        twoLetterCount += 1 if twoLetterMatch else 0
        threeLetterCount += 1 if threeLetterMatch else 0

    print(twoLetterCount * threeLetterCount)

if __name__ == '__main__':
    main()