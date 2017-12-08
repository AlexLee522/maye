def bin_search(key):
    a = [32, 24, 15, 23, 63, 34, 54, 23, 34, 35, 12, 2, 7, 65, 58]
    b = sorted(a)
    low = 0
    high = len(a)-1
    while low <= high:
        mid = (low + high)/2
        if key == b[mid]:
            return a.index(key)
        elif key < b[mid]:
            high = mid-1
        elif key > b[mid]:
            low = mid+1


c = int(input('please input a number:'))
d = bin_search(c)
if type(d) == type(123):
    print 'it\'s index is %d' % d
else:
    print 'this number is not in the list.'
    
