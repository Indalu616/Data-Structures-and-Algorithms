# Problem: Number of smaller - https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/B


n,m=map(int,input().split())

arr1=list(map(int,input().split()))

arr2=list(map(int,input().split()))

answer=[]

p1=0
p2=0

count=0
while p2 < m:
    
    if p1 < n and arr1[p1] < arr2[p2]:
        count+=1
        p1+=1
    else:
        answer.append(count)
        p2+=1
print(*answer)