import math

def need(n,x):
    if n == 0:
        a = square_area(x)
        return 'it\'s %d' % a
    if n == 1:
        a = circle_area(x)
        return 'it\'s %.2f' % a
    if n == 2:
        a = regular_triangle_area(x)
        return 'it\'s %.2f' % a
    else:
        return 'sorry,please input the right number.'


def square_area(x):
    a = x*x
    return a

def circle_area(x):
    a = 3.14*x*x
    return a

def regular_triangle_area(x):
    a = round(math.sqrt(3)*x*x/4,2)
    return a

x = int(input('please input a number:'))
n = int(input('square area:0\ncircle area:1\nregular triangle area:2\n'))
print need(n,x)



