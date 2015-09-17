import csv
import argparse
import sys

def LCS(x, y):
    m, n = len(x), len(y)
    b = [[0 for i in range(n + 1)] for j in range(m + 1)]
    c = [[0 for i in range(n + 1)] for j in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
                b[i][j] = 0
            elif c[i - 1][j] >= c[i][j - 1]:
                c[i][j] = c[i - 1][j]
                b[i][j] = 1
            else:
                c[i][j] = c[i][j - 1]
                b[i][j] = 2
    return b, c

def DiffWithRecursion(b, x, y, i, j):
    diff = []
    if i > 0 and j > 0 and b[i][j] == 0:
        diff = Diff(b, x, y, i - 1, j - 1)
        diff.append((x[i - 1], " "))
    elif i > 0 and (j == 0 or b[i][j] == 1):
        diff = Diff(b, x, y, i - 1, j)
        diff.append((x[i - 1], "-"))
    elif j > 0 and (i == 0 or b[i][j] == 2):
        diff = Diff(b, x, y, i, j - 1)
        diff.append((y[j - 1], "+"))
    else:
        pass
    return diff

def DiffWithoutRecursion(b, x, y, i, j):
    diff = []
    while i > 0 and j > 0:
        if b[i][j] == 0:
            diff.append((x[i - 1], " "))
            i -= 1
            j -= 1
        elif b[i][j] == 1:
            diff.append((x[i - 1], "-"))
            i -= 1
        else:
            diff.append((y[j - 1], "+"))
            j -= 1
    while i > 0:
        diff.append((x[i - 1], "-"))
        i -= 1
    while j > 0:
        diff.append((y[j - 1], "+"))
        j -= 1
    return diff[::-1]

def CommWithRecursion(b, x, i, j):
    comm = []
    if i == 0 or j == 0:
        return comm
    elif b[i][j] == 0:
        comm = CommWithRecursion(b, x, i - 1, j - 1)
        comm.append(x[i - 1])
    elif b[i][j] == 1:
        comm = CommWithRecursion(b, x, i - 1, j)
    else:
        comm = CommWithRecursion(b, x, i, j - 1)
    return comm

def CommWithoutRecursion(b, x, i, j):
    comm = []
    while i > 0 and j > 0:
        if b[i][j] == 0:
            comm.append(x[i - 1])
            i -= 1
            j -= 1
        elif b[i][j] == 1:
            i -= 1
        else:
            j -= 1
    return comm[::-1]

def CsvDiff(filename1, fieldname1, filename2, fieldname2, result="DIFF.csv"):
    with open(filename1) as fp1, open(filename2) as fp2:
        reader1 = csv.DictReader(fp1)
        reader2 = csv.DictReader(fp2)
        field1 = [row[fieldname1] for row in reader1]
        field2 = [row[fieldname2] for row in reader2]
        b, c = LCS(field1, field2)
        diff = DiffWithoutRecursion(b, field1, field2, len(field1), len(field2))
        with open(result, "w") as res:
            fieldnames = ["CONTENT", "OPERATE"]
            writer = csv.DictWriter(res, fieldnames, lineterminator="\n")
            writer.writeheader()
            for item in diff:
                writer.writerow({"CONTENT": item[0], "OPERATE": item[1]})

def CsvComm(filename1, fieldname1, filename2, fieldname2, result="COMM.csv"):
    with open(filename1) as fp1, open(filename2) as fp2:
        reader1 = csv.DictReader(fp1)
        reader2 = csv.DictReader(fp2)
        field1 = [row[fieldname1] for row in reader1]
        field2 = [row[fieldname2] for row in reader2]
        b, c = LCS(field1, field2)
        comm = CommWithoutRecursion(b, field1, len(field1), len(field2))
        with open(result, "w") as res:
            fieldnames = ["COMMON"]
            writer = csv.DictWriter(res, fieldnames, lineterminator="\n")
            writer.writeheader()
            for item in comm:
                writer.writerow({"COMMON": item})

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("csv1", help="the old csv file")
    parser.add_argument("field1", help="the field name of old csv file")
    parser.add_argument("csv2", help="the new csv file")
    parser.add_argument("field2", help="the field name of new csv file")
    parser.add_argument("-o", "--output", action="store", 
        help="save result in csv file")
    parser.add_argument("-c", "--common", action="store_true", 
        help="compute the longest common sequence of two fields")
    args = parser.parse_args()
    if args.common:
        print("running comm...")
        if args.output:
            CsvComm(args.csv1, args.field1, args.csv2, args.field2, args.output)
        else:
            CsvComm(args.csv1, args.field1, args.csv2, args.field2)
    else:
        print("running diff...")
        if args.output:
            CsvDiff(args.csv1, args.field1, args.csv2, args.field2, args.output)
        else:
            CsvDiff(args.csv1, args.field1, args.csv2, args.field2)

if __name__ == "__main__":
    main()
