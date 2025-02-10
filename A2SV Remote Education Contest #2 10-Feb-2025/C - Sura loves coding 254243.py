# Problem: C - Sura loves coding - https://codeforces.com/gym/586622/problem/C

n=int(input())

encoded=input()

decoded=""

if n%2:
    for i in range(n):
        if i%2:
            decoded=encoded[i]+decoded
        else:
            decoded+=encoded[i]
else:
    for i in range(n):
        if i%2:
            decoded+=encoded[i]
        else:
            decoded=encoded[i]+decoded
            
print(decoded)