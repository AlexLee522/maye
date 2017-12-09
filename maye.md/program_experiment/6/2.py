# coding=utf-8
# 最大公约数

def greatest_common_divisor(a,b):
    a,b = b%a,a
    if a == 0:
        return b
    else:
        return greatest_common_divisor(a,b)

a,b = map(int,raw_input('please input two numbers:').split(','))
print 'the greatest common divisor is %d' % greatest_common_divisor(a,b)
