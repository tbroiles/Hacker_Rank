
from collections import Counter

X = int(raw_input())

shoes = [int(i) for i in raw_input().split(' ')]

dist_shoes = Counter(shoes)

n_buyers = int(raw_input())
income = 0
for b in xrange(n_buyers):
    
    buyer = [int(i) for i in raw_input().split(' ')]
    if dist_shoes[buyer[0]] > 0:
        income += buyer[1]
        dist_shoes[buyer[0]] -= 1
        
print income
