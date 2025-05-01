# Problem: Print 1 to n without using loops - https://www.geeksforgeeks.org/print-1-to-n-without-using-loops/

def printNum(num):
    if num > 0:
        printNum(num - 1)
        print(num, end=' ')