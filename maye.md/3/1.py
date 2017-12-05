num=eval(input("请输入学生数量"))
if num>50:
    print("错误，请重新输入")
else:
    m=1
    sum=0
    while m<=num:
        i=eval(input("请输入成绩"))
        sum+=i
        m=m+1
    print("学生平均成绩为",sum/num)
