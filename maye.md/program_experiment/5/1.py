def average(x):
    avg = sum(x)/3
    return avg


i = 1
x = []
while i < 4:
    s = []
    name = raw_input('input student\'s name:')
    n = raw_input('input student\'s score:')
    tem = map(eval, n.split())
    s.append(tem)
    s.append(average(tem))
    total = sum(tem)
    score = s
    p = [name, score, total] 
    x.append(p)
    i += 1
print sorted(x, key=lambda y: y[2])

