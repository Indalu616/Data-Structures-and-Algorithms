# Problem: C - Robin’s Water Wisdom: Stop the Leaks! - https://codeforces.com/gym/594356/problem/C

def min_holes_to_block(n, A, B, sizes):
    S = sum(sizes)  # Total sum of hole sizes
    s1 = sizes[0]   # First hole size
    required_S = (s1 * A) / B  

    if S <= required_S:
        return 0  

    other_holes = sorted(sizes[1:], reverse=True) 
    blocked = 0

    for size in other_holes:
        S -= size
        blocked += 1
        if S <= required_S:
            break
    
    return blocked


n, A, B = map(int, input().split())
sizes = list(map(int, input().split()))


print(min_holes_to_block(n, A, B, sizes))
