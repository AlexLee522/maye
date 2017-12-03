a = input('please input a list:')
b = int(input('target:'))
c = sorted(a)
left = 0
right =len(a) - 1
while left < right:
    sum_number = c[left] + c[right]
    if sum_number == b:
        break
    elif sum_number > b:
        right -= 1
    elif sum_number < b:
        left += 1
if left == right :
    print 'wrong'
else:
    p1 = a.index(c[left])
    p2 = a.index(c[right])
print [p1,p2]

