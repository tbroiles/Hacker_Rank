
n = xrange(int(raw_input()))
strings = []
for i in n:
    strings.append(raw_input())
    
t = xrange(int(raw_input()))

for j in t:
    word = raw_input()
    murca_word = word.replace('our', 'or')
    print sum([i.split().count(word) for i in strings]) + sum([i.split().count(murca_word) for i in strings])
