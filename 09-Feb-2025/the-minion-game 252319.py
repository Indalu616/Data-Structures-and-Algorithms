# Problem: the-minion-game - https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true

def minion_game(string):
    # your code goes here
    vowels="AEIOU"
    kevin_total=0
    st_total=0
    
    n=len(string)
    
    for i in range(n):
        if string[i] in vowels:
            kevin_total+=n-i
        else:
            st_total+=n-i
            
    if kevin_total > st_total:
        print(f"Kevin {kevin_total}")
    elif kevin_total < st_total:
        print(f"Stuart {st_total}")
    else:
        print("Draw")