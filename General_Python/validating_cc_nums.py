


import re

N = int(raw_input())

pattern = re.compile('[4-6]\d\d\d-?\d\d\d\d-?\d\d\d\d-?\d\d\d\d')

repeat_pattern = re.compile("(\\d)\\1{3,}")

for i in xrange(N):
    cc = raw_input()
    if pattern.match(cc):
        cc = cc.replace('-', '')
        if len(cc) == 16:
            if repeat_pattern.search(cc):
                print 'Invalid'
            else:
                print 'Valid'
        else:
            print 'Invalid'
    else:
        print 'Invalid'
