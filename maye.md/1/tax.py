a = input('enter your salary:')
if 0 < a < 50000 :
    tax = a * 0.05
    print tax
elif 50000 < a <100000 :
    tax = 2500 + (a-50000)*0.07
    print tax
elif a >= 100000 :
    tax = 6000 + (a-100000)*0.09
    print tax
elif a < 0 :
    print 'please input a positive number'

