a = input()
n = len(a)
for i in range(n-1):
    flag = 0
    for j in range(n-1-i):
        if a[j] > a[j+1]:
            a[j+1],a[j] = a[j],a[j+1]
            flag = 1
    if flag == 0:
        break
print a
