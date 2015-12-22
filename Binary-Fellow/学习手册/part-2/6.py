# -*- coding: cp936 -*-
#字典索引运算
#

from echo import echo
echo(__file__)

D = {'a':1,'b':2,'c':3}

#试图索引不存在的键值，会报错
try:
   print D['d']
except:
   print "SOME ERROR"

#对不存在的索引赋值会生成新键
try:
   D['d'] = 'spam'
   print D
except:
   print "SOME ERROR"

#列表不能对边界以外的值进行赋值
l = [1,2,3]
try:
   l[5] = 23
   print l
except:
   print "SOME ERROR"




