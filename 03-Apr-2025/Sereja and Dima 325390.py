# Problem: Sereja and Dima - https://codeforces.com/problemset/problem/381/A


n=int(input())

nums=list(map(int,input().split()))

left=0

right=len(nums)-1

sereja=0
dima=0
turn=1

while left <= right:
    
    if turn %2:
        if nums[left] >=nums[right]:
            dima+=nums[left]
            left+=1
            turn+=1
        else:
            dima+=nums[right]
            right-=1
            turn+=1
    else:
        if nums[left] >=nums[right]:
            sereja+=nums[left]
            left+=1
            turn+=1
        else:
            sereja+=nums[right]
            right-=1
            turn+=1
print(dima, sereja)
        