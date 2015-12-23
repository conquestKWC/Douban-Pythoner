# -*- coding: cp936 -*-
from echo import echo
echo(__file__)

#读入一个字典，给字典的每个元素赋值
def copydict(Dict):
   temp = {}
   if type(Dict) == dict:
      for x in Dict:#遍历字典的键值
         temp[x] = 0#赋值部分
   return temp
#返回一个新字典，不改变原字典

d = {'a':123,'b':234,'c':345,'d':456}

#不能用序列d[:]顶层复制，类型不符合
#1)
print copydict(d)
#2)
try:
   temp = d[:]
   print temp
except:
   print "Error"
