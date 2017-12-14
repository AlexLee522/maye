def move(n,x,y,z):
    if n == 1:
        print 'move:',x,'-->',z
    else:
        move(n-1,x,z,y)
        move(1,x,y,z)
        move(n-1,y,x,z)


move(3,'A','B','C')
