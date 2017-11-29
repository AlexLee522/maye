a = input('please enter a list:')
b = input('please enter a target number:')
for i in range (len(a)) :
    for j in range (len(a)) :
        if a[i] + a[j] == b and j > i :
            m = [i,j]
            print m
