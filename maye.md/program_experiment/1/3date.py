#-*- coding:utf-8 -*-
a,b,c = input('请输入日期:')
m = 0
r = (a-2000) % 4
if b > 12 or c > 31:
    print 'error'
elif r == 0 and b == 2 and c > 29:
    print 'error'
elif r != 0 and b == 2 and c > 28:
    print 'error'
else:
    if r == 0 or a % 400 == 0:
        ms = [31,29,31,30,31,30,31,31,30,31,30,31]
    if r != 0 or a % 400 != 0:
        ms = [31,28,31,30,31,30,31,31,30,31,30,31]
    for i in range(0,13):
        if i+1 < b :
            m += ms[i]
    n = m + c
    print '这一天是这一年的第%d天'%n
