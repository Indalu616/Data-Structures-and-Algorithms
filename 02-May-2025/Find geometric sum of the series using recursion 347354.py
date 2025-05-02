# Problem: Find geometric sum of the series using recursion - https://www.geeksforgeeks.org/find-geometric-sum-of-the-series-using-recursion/

n=int(input())
def findGeom(n):
    
    if n==0:
        return 1
    
    return 1/(3**n)+findGeom(n-1)

print(findGeom(n))