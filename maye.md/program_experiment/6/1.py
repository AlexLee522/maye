def average(l):
    avg = float(sum(l))/float(len(l))
    return avg


def number(l):
    n = 0
    for i in l:
        if i > average(l):
            n += 1
    return n


l = input('input a list:')
avg = average(l)
print 'average is %.2f' % avg
num = number(l)
print 'more than average:%d' % num

