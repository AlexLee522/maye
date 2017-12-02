def insert_sort(l):
    assert(type(l) == type(['']))
    count = len(l)
    if count == 0 or count == 1:
        return l
    for i in range(count):
        key = l[i]
        j = i-1
        while j >=0 and l[j] > key:
                l[j+1] = l[j]
                j -= 1
        l[j+1] = key
    return l

l = input()
insert_sort(l)
print l
