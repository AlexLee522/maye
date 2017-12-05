s = raw_input('please input:')
blankcount = 0
integercount = 0
lettercount = 0
othercount = 0
for i in s :
    if ord(i) == 32:
        blankcount += 1
    elif 47 < ord(i) < 58:
        integercount += 1
    elif 64 < ord(i) < 107 or 96 < ord(i) < 123:
        lettercount += 1
    else:
        othercount += 1
print 'blankcount = %d,integercount = %d,lettercount = %d,othercount = %d' % (blankcount,integercount,lettercount,othercount)


