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
    
# Example

file1.csv

    Date,Open,High,Low,Close,Volume
    2015/8/31,112.13,114.53,112,112.76,56229271
    2015/8/28,112.17,113.31,111.54,113.29,53164407
    2015/8/27,112.25,113.24,110.02,112.92,84616056
    2015/8/26,107.085,109.89,105.05,109.69,96774611
    2015/8/25,111.11,111.11,103.5,103.74,103601599
    2015/8/24,94.87,108.8,92,103.12,162206292
    2015/8/21,110.43,111.9,105.645,105.76,128275471
    2015/8/20,114.08,114.35,111.63,112.65,68501622
    
file2.csv

    Date,Bullish Intensity,Bearish Intensity,Bull - Bear,Bullish Messages,Bearish Messages
    2015/8/31,1.803829,2.007308,-0.203478,363,156
    2015/8/30,1.844899,2.116458,-0.271559,149,48
    2015/8/29,1.921223,1.98913,-0.067907,139,46
    2015/8/28,1.800461,1.943976,-0.143515,369,166
    2015/8/27,1.891543,1.832338,0.059205,499,278
    2015/8/26,1.781992,2.186308,-0.404315,532,390
    2015/8/25,1.895249,1.866114,0.029135,802,332
    2015/8/24,1.792849,1.898614,-0.105765,1576,938
    2015/8/23,1.937114,2.106379,-0.169265,298,116
    2015/8/22,1.85802,2.166091,-0.308071,202,110
    2015/8/21,1.754635,2.058819,-0.304184,643,838
    2015/8/20,1.671921,2.021962,-0.350042,328,372
    2015/8/19,2.108477,2.133966,-0.025489,348,174

Compute "Date" column difference of file1 and file2:

    python csvdiff.py file1.csv Date file2.csv Date

Results are exported into DIFF.csv

    CONTENT,OPERATE
    2015/8/31, 
    2015/8/30,+
    2015/8/29,+
    2015/8/28, 
    2015/8/27, 
    2015/8/26, 
    2015/8/25, 
    2015/8/24, 
    2015/8/23,+
    2015/8/22,+
    2015/8/21, 
    2015/8/20, 
    2015/8/19,+

Compute the longest common sequence of "Date" column:

    python csvdiff.py file1.csv Date file2.csv Date

Results are exported into COMM.csv

    COMMON
    2015/8/31
    2015/8/28
    2015/8/27
    2015/8/26
    2015/8/25
    2015/8/24
    2015/8/21
    2015/8/20
