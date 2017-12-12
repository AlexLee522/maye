#python3.6
import codecs
name = input('请输入文件名：')
from_file = codecs.open(name,encoding='utf-8').read()
count = 0
f = from_file.split()
input_name = input('请输入要查找的姓氏：')
for i in f:
    if input_name == i[0]:
        print (i,end=' ')
        count += 1
print (count)
