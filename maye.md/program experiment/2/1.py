sum=0
n=eval(input("the amount of all the numbers is:"))
if n>10:
    print("Erro")
    n=eval(input("the right amount of all the number is:"))
for i in range(0,n):
    a=eval(input("the number is:"))
    sum=sum+a
print("the sum is %d"%sum)

