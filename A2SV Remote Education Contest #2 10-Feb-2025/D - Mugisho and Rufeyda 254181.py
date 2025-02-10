# Problem: D - Mugisho and Rufeyda - https://codeforces.com/gym/586622/problem/D

nums=list(map(int,input().split()))

n=nums[0]
t=nums[1]

lower=10**(n-1)
upper=10**n
is_found=False

while lower < upper:
    if lower % t==0 and lower >0:
        print(lower)
        is_found=True
        break
    lower+=1

if not is_found:
    print(-1)