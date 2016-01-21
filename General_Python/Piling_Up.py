
from collections import deque

T = int(raw_input())

for test in xrange(T):
    N = int(raw_input())
    blocks = deque([long(i) for i in raw_input().split()])
    flag = True
    old = max(blocks)
    for i in xrange(N):
        if max((blocks[0],blocks[-1])) > old:
            flag = False
            break
        else:
            if blocks[0] > blocks[-1]:
                old = blocks.popleft()
            else:
                old = blocks.pop()
    if flag:
        print 'Yes'
    else:
        print 'No'
