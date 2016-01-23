

from collections import defaultdict, deque
        
T = int(raw_input())

for trial in xrange(T):
    
    g = defaultdict(set)
    search = deque()
    distances = defaultdict(int)
    
    nodes, edges = [int(i) for i in raw_input().split()]
    
    for edge in xrange(edges):
        node1, node2 = [int(i) for i in raw_input().split()]
        g[node1].add(node2)
        g[node2].add(node1)

    
    S = int(raw_input().strip())
    for node in xrange(1,nodes+1):
        if node != S:
            distances[node] = -1
    for n in g[S]:
        distances[n] = 6
    search.extendleft(g[S])
    while len(search) > 0:
        pos = search.pop()
        while len(g[pos]) > 0:
            n = g[pos].pop()
            if n != S and distances[n] < 0:
                distances[n] = distances[pos]+6
                search.appendleft(n)
                

    print ' '.join([str(distances[i]) for i in sorted(distances.keys())])
