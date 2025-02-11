# Problem: E - The beautiful String - https://codeforces.com/gym/586622/problem/E

t = int(input().strip())

for _ in range(t):
    word = input().strip()
    n = int(input().strip())
    chars = list(word)

    # Precompute the count of "1100" in the string
    count_1100 = sum(1 for i in range(len(word) - 3) if word[i:i+4] == "1100")

    for _ in range(n):
        idx, el = map(int, input().strip().split())
        idx -= 1  # Convert to zero-based index
        
        # Check if the update affects any existing "1100"
        affected_ranges = range(max(0, idx - 3), min(len(chars) - 3, idx) + 1)
        old_count = count_1100

        # Remove old occurrences of "1100" in affected range
        for i in affected_ranges:
            if "".join(chars[i:i+4]) == "1100":
                count_1100 -= 1

        # Apply the update
        chars[idx] = str(el)

        # Recheck for new occurrences of "1100" in affected range
        for i in affected_ranges:
            if "".join(chars[i:i+4]) == "1100":
                count_1100 += 1

        print("YES" if count_1100 > 0 else "NO")