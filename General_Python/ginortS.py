
import re

string = raw_input()

print '%s'*len(string) % tuple(sorted(string, key = lambda x: ( re.sub('[^0,2,4,6,8]','',x),
                                                                re.sub('[^1,3,5,7,9]','',x),re.sub('[^A-Z]','',x),
                                                                re.sub('[^a-z]','',x))))
