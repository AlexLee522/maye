def guess(n):
    import random
    a = random.randint(1,11)
    for i in range(3):
        n = int(input('your number:'))
        if n == a :
            print 'Congratulations!'
            break
        else :
            if n > a :
                print 'It is a little higher'
            elif n < a :
                print 'It is a little lower'
    print 'It is over.Try again(1) or stop(0)?'

n = 0
guess(n)
m = input()
x = 1
while m == 0 :
    print 'thank you'
    print 'total time = %d' % x
    break
while m == 1 :
    guess(n)
    x += 1
    m = input()
    if m == 1 :
        continue
    else:
        print 'thank you'
        print 'total time = %d' % x
        break
