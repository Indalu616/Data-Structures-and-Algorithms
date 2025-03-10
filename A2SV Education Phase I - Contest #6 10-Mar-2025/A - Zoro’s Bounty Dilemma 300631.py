# Problem: A - Zoro’s Bounty Dilemma - https://codeforces.com/gym/594356/problem/A

def determine_bounty_relationship(test_cases):
    results = []
    for s in test_cases:
        has_less = '<' in s
        has_greater = '>' in s
        
        if has_less and has_greater:
            results.append('?')
        elif has_less:
            results.append('<')
        elif has_greater:
            results.append('>')
        else:
            results.append('=')
    
    return results

# Read input
t = int(input())
test_cases = [input().strip() for _ in range(t)]

for result in determine_bounty_relationship(test_cases):
    print(result)