#!/usr/bin/python

def main():
    file = open("input.txt", "r")
    input = file.readlines()
    for comparer in input:
        comparer = comparer.strip()
        for comparee in input:
            comparee = comparee.strip()
            nonMatchingIndexes = [i for i in range(len(comparer)) if comparer[i] != comparee[i]]
            if (len(nonMatchingIndexes) == 1):
                print(comparer[:nonMatchingIndexes[0]] + comparer[nonMatchingIndexes[0]+1:])
                return

if __name__ == '__main__':
    main()