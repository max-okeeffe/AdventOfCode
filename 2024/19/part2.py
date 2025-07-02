import numpy as np

filename = input() + ".txt"
towels, patterns = open(filename).read().split('\n\n')
towels, patterns = towels.split(', '), patterns.split()

dp = {}

def possible(pattern):
    if pattern in dp:
        return dp[pattern]
    
    if pattern == '':
        return True
    
    if len(pattern) == 1:
        return 1 if pattern in towels else 0
    
    for towel in towels:
        if pattern.startswith(towel) and possible(pattern[len(towel):]):
            dp[pattern] = True
            return True

    dp[pattern] = False  
    return False

def irreducible(pattern):
    if pattern == '':
        return True
    
    if pattern not in towels:
        return False
    
    for towel in towels:
        if len(towel) < len(pattern) and pattern.startswith(towel) and possible(pattern[len(towel):]):
            return False
        
    return True

countdp = {}
def count(pattern):
    if pattern in countdp:
        return countdp[pattern]
    
    if not possible(pattern):
        countdp[pattern] = 0
        return 0
    
    if irreducible(pattern):
        countdp[pattern] = 1
        return 1
    
    total = 0
    for towel in towels:
        if pattern.startswith(towel):
            newpattern = pattern[len(towel):]
            total += count(newpattern)
    countdp[pattern] = total
    return total

print(sum(count(pattern) for pattern in patterns))
