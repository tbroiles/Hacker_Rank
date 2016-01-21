
h = int(raw_input())
m = int(raw_input())

num_words = {1:'one ',2:'two ',3:'three ',4:'four ',5:'five ',6:'six ',7:'seven ',8:'eight ',9:'nine ',
             10:'ten ',11:'eleven ',12:'twelve ',13:'thirteen ',14:'fourteen ',15:'quarter ',
             16:'sixteen ',17:'seventeen ', 18:'eighteen ',19:'nineteen ',20:'twenty ',21:'twenty one ',
             22:'twenty two ',23:'twenty three ',24:'twenty four ',25:'twenty five ',26:'twenty six ',
             27:'twenty seven ',28:'twenty eight ',29:'twenty nine ',30:'half '}

if m > 30:
    m = 60-m
    h+=1
    connector = 'to '
else:
    connector = 'past '

if m == 1:
    m_unit = 'minute '
elif m == 15 or m == 30:
    m_unit = ''
else:
    m_unit = 'minutes '
    
if m == 0:
    print num_words[h] + "o' clock"
else:
    print num_words[m]+m_unit+connector+num_words[h]
