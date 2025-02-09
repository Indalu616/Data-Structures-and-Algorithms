# Problem: Same Differences - https://codeforces.com/problemset/problem/1520/D

t=int(input())
for i in range(t):
    n=int(input())
    nums=list(map(int,input().split()))
    freq={}
    count=0
    for j in range(n):
        key=nums[j]-j
        if key in freq:
            freq[key]+=1
            count+=freq[key]
        else:
            freq[key]=0
    print(count)