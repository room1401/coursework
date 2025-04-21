'''
Please write a function named words(n: int, 
beginning: str), which returns a list containing 
n random words from the words.txt file. All words 
should begin with the string specified by the 
second argument.

The same word should not appear twice in the list. 
If there are not enough words beginning with the 
specified string, the function should raise a 
ValueError exception.
'''

# Write your solution here
from random import sample

def words(pick, pref):
    pool = []
    with open("words.txt") as file:
        for line in file:
            if line.startswith(pref):
                pool.append(line.rstrip())
            elif pool:
                break
    
    if len(pool) < pick:
        raise ValueError
    
    return sample(pool, pick)
