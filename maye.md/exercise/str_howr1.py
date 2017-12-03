def x(a,b):
    assert(len(a)<10000)
    assert(len(b)<10000)
    if b in a and len(a) == len(b):
        return 1
    n = 1
    while a in b :
        if b in a*n:
            return n
        else:
            n += 1
    else:
        return -1
a = raw_input()
b = raw_input()
print x(a,b)

