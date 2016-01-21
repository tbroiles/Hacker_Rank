

N = int(raw_input())
K = int(raw_input())
lists = [int(raw_input()) for _ in xrange(0,N)]
lists.sort()
min_diff = max(lists) - min(lists)
if K%2 == 0:
    neg_k = int(K/2)
    pos_k = int(K/2)-1
else:
    neg_k = int(K/2)
    pos_k = int(K/2)
for i in xrange(neg_k, N-pos_k):
    if lists[i+pos_k] - lists[i-neg_k]< min_diff:
        min_diff = lists[i+pos_k] - lists[i-neg_k]

print min_diff
