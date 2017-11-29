s = raw_input('please input:')
bankcount = 0
integercount = 0
lettercount = 0
othercount = 0
for i in s :
    if ord(i) == 32:
        bankcount += 1
    elif 47 < ord(i) < 58:
        integercount += 1
    elif 64 < ord(i) < 107 or 96 < ord(i) < 123:
        lettercount += 1
    else:
        othercount += 1
print 'bankcount = %d,integercount = %d,lettercount = %d,othercount = %d' % (bankcount,integercount,lettercount,othercount)


