s="我/是/一个/测试/句子/,/大家/赶快/来/统计/我/吧/,/大家/赶快/来/统计/我/吧/,/大家/赶快/来/统计/我/吧/,/重要/事情/说/三遍/!"
a=s.split("/")
for i in a:
    if i==','or i=='!':
        a.remove(i)        
dict={}
for m in a:
    dict[m]=dict.get(m,0)+1
print(dict,len(dict))
