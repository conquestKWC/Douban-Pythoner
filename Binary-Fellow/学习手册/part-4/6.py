# -*- coding: cp936 -*-
from echo import echo
echo(__file__)
from test import *
#从测试模块读入两个字典，打印整个代码

def addict(dict1, dict2):
   temp = dict2
   for x in dict1:
      if x not in dict2:
         temp[x]=dict1[x]
   return temp

def add_u(one, two):
   if type(one) == type(two):
      if type(one) == dict:
         temp = two.copy()
         for x in one:
            if x not in two:
               temp[x]=one[x]
         return temp
      elif type(one) == str:
         temp = two
         for x in one:
            if x not in two:
               temp+=x
         return temp
      elif type(one) == list:
         temp = two[:]
         for x in one:
            if x not in two:
               temp.append(x)
         return temp
      elif type(one) == tuple:
         #因为元组的特殊性，不能在原处修改，只能借助于列表，最后转换为元祖
         temp = list(two)
         for x in one:
            if x not in two:
               temp.append(x)
         return tuple(temp)
      else:
         return two+one#单个数字的相加
   else:
      print "can't add two different type"

print addict(d1,d1)
#不通用化
try:
   print addict(l1,l2)
except:
   print "out range of index"
#通用化
print add_u(l1,l2),add_u(t2,t1),add_u(s1,s2),add_u(d1,d2)
