str1=input("Please input the first string:")
str2=input("Please input the second string:")
if(str1>str2):
    print("the bigger one is:"+str1)
elif(str1==str2):
    print("字符串相同")
else:
    print("the bigger one is:"+str2)

    
str1=str(input("请输入原字符串:"))
str2=str(input("请输入要追加的字符串:"))
list1=[str1,str2]
print(''.join(list1))


str1=str(input('输入要拷贝的字符串:'))
list1=[str1]
list2=list1.copy()
str2=''.join(list2)
print(str2)
