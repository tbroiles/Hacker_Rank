
from collections import defaultdict

n, m = [int(i) for i in raw_input().split(' ')]
A = defaultdict(list)

for i in xrange(n):
    A[raw_input()].append(str(i+1))

for i in xrange(m):
    index = A[raw_input()]
    if len(index) != 0:
        print ' '.join(index)
    else:
        print '-1'
