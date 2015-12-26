# -*- coding: cp936 -*-
from echo import echo
echo(__file__)
from math import sqrt
#for
def ForSqrt(List):
   temp =[]
   if type(List) == list:
      for x in List:
         temp.append(sqrt(x))
   return temp
#map
def MapSqrt(List):
   if type(List) == list:
      return map(lambda x:sqrt(x),L)
#列表解析
def ListSqrt(List):
   if type(List) == list:
      return [sqrt(x) for x in L]

#列表解析会更方便
   #1.直观
   #2.比起用for会更快
   #3.map当function部分不是内置的时候，性能表现甚至会连for都不如

L = [2,4,9,16,25]

print ForSqrt(L)
print MapSqrt(L)
print ListSqrt(L)

         
