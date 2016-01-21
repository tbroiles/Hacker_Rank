
from collections import Counter

string = raw_input()

c = Counter(string)
c_sort = sorted(c, key = lambda x: (1./c[x],x))
for i in c_sort[0:3]:
    print ' '.join([i,str(c[i])])
