def bubble_sort(l):
    assert(type(l) == type(['']))
    length = len(l)
    if length == 0 or length == 1:
        return l
    for i in range(length):
        for j in range(length-1-i):
            if  l[j] > l[j+1]:
                temp = l[j]
                l[j] = l[j+1]
                l[j+1] = temp
    return l

l = input()
bubble_sort(l)
print l
                

