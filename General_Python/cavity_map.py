

n = int(raw_input())
m = []
for i in xrange(n):
    m.append([str(i) for i in raw_input()])
    
for j in xrange(1,n-1):
    for k in xrange(1,n-1):
        if m[j][k] > m[j][k+1] and m[j][k] > m[j][k-1] and m[j][k] > m[j+1][k] and m[j][k] > m[j-1][k]:
            m[j][k] = 'X'

for l in xrange(n):
    print ''.join(m[l])
