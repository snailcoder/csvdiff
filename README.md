# csvdiff

This is a special but simple diff implemented in Python3.4 for processing CSV file.

Maybe you're looking for a tool to compare two fields in two CSV files and wanna find out their common part or difference, 
that's just the job of this tiny toy!

The basic idea behind csvdiff.py is finding the longest common sequence(LCS) of two fields in two CSV files. As you know, there's
a clean solution with dynamic programming method.

# Usage

csvdiff.py  [-h]  [-o OUTPUT]  [-c]  csv1  field1  csv2  field2

positional arguments:

    csv1                  the old csv file
    field1                the field name of old csv file
    csv2                  the new csv file
    field2                the field name of new csv file

optional arguments:

    -h, --help            show this help message and exit
    -o OUTPUT, --output OUTPUT save result in csv file
    -c, --common          compute the longest common sequence of two fields
