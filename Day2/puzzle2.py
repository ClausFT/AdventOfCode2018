#!/usr/bin/python

def main():
    file = open("input.txt", "r")
    input = [i.strip() for i in file.readlines()]
    for comparer in input:
        for comparee in input:
            non_matching_indexes = [i for i in range(len(comparer)) if comparer[i] != comparee[i]]
            if (len(non_matching_indexes) == 1):
                print(comparer[:non_matching_indexes[0]] + comparer[non_matching_indexes[0]+1:])
                return

if __name__ == '__main__':
    main()