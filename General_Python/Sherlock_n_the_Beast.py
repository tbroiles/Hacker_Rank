
t = xrange(int(raw_input()))

for i in t:
    N = int(raw_input())

    tmp = N 
    while (tmp%3 != 0): 
        tmp -=5
    
    if (tmp < 0):
        print -1
    else:
        print int('5'*tmp+'3'*(N-tmp))
