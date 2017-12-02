a = [25,28,76,89,90,100]
x = input()
t = 0
for i in a:
    if x < i:
        a.insert(t,x)
        break
    else:
        t += 1
print a
