#!/usr/bin/python
import csv

def main():
    result = {}

    with open('compass-tap-outs.csv', 'rb') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in csvreader:
            if row[0] in result:
                result[row[0]].append(row[1])
            else:
                result[row[0]] = [row[1]]

    for datekey in result.items():
        print "{},{}".format(datekey[0], len(datekey[1]))

if __name__ == '__main__':
    main()
