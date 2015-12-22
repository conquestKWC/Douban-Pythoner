# -*- coding: cp936 -*-
#排序字典

d = {'h':1,'b':2,'c':3,'d':4}
#内置sorted方法
print sorted(d)
l = d.keys()
#keys方法获取关键字列表用sort进行排序
l.sort()
print l

#将关键字和值转换为一个元组，加入列表ld中，对ld进行排序，ld可以直接转化为字典，取用也很方便
ld = []
for i in l:
   ld.append((i,d[i]))
ld.sort()
print ld

