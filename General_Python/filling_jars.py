
n, m = [int(i) for i in raw_input().split()]

total = 0

for i in xrange(m):
    a, b, k = [int(i) for i in raw_input().split()]
    total += ((b-a)+1)*k
    
print int(total/n)
