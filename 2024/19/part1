import numpy as np

filename = input() + ".txt"
towels, patterns = open(filename).read().split('\n\n')
towels, patterns = towels.split(', '), patterns.split()

dp = {}
for towel in towels:
    dp[towel] = True

def possible(pattern):
    if pattern in dp:
        return dp[pattern]
    
    for towel in towels:
        if pattern.startswith(towel) and possible(pattern[len(towel):]):
            dp[pattern] = True
            return True

    dp[pattern] = False  
    return False

print(sum(possible(pattern) for pattern in patterns))
