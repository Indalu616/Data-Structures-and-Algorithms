# Problem: A. Beautiful Matrix - https://codeforces.com/problemset/problem/263/A

for i in range(5):
    
    nums=list(map(int,input().split()))
    is_found=False
    
    for j in range(len(nums)):
        if nums[j]==1:
            print(abs(i-2)+abs(j-2))
            is_found=True
            break
    if is_found:
        break