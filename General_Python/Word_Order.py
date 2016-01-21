
from collections import OrderedDict

N = int(raw_input())
c = OrderedDict()

for i in xrange(N):
    word = raw_input()
    if c.has_key(word):
        c[word] += 1
    else:
        c[word] = 1

print len(c)
print ' '.join([str(i) for i in c.values()])
