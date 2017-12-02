def select_sort(l):
    assert(type(l) == type(['']))
    length = len(l)
    if length == 0 or length == 1:
        return l

    def minnumber(a):
        minimum = a
        for i in range(a,length):
            if l[i] < l[minimum]:
                minimum = i
        return minimum
    for i in range(length):
        minimum = minnumber(i)
        if i != minimum:
            temp = l[minimum]
            l[minimum] = l[i]
            l[i] = temp
    return l

l = input()
select_sort(l)
print l


