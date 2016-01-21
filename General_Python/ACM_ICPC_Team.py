
import itertools

peeps, topics = [int(i) for i in raw_input().split()]
knowledge = []

for i in xrange(peeps):
    knowledge.append(int(raw_input(),2))
    
teams = 0
max_tk = 0
for j, k in itertools.combinations(xrange(peeps),2):
    tk = bin(knowledge[j]|knowledge[k]).count('1')
    if tk > max_tk:
        max_tk = tk
        teams=1
    elif tk == max_tk:
        teams+=1

        
print max_tk
print teams
