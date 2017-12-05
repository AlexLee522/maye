# coding=utf-8
count=1
passer=great=fail=0
scores=[]
while count<=30:
    scores.append(int(input("Enter the student's score:")))
    count+=1
for i in scores:
    if  60<=i<90:
        passer+=1
    elif  i>=90:
        great+=1
    else:
        fail+=1
print 'passer:%d excellent:%d failed:%d' % (passer,great,fall)

