a = {0:2,1:7,2:11,3:15}
b = int(input('target:'))
for i in a:
    for j in range(i,4):
        if a[i] + a[j] ==b:
            x = [i,j]
            print x

