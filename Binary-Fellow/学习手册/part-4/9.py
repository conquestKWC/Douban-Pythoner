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
#�б����
def ListSqrt(List):
   if type(List) == list:
      return [sqrt(x) for x in L]

#�б�����������
   #1.ֱ��
   #2.������for�����
   #3.map��function���ֲ������õ�ʱ�����ܱ�����������for������

L = [2,4,9,16,25]

print ForSqrt(L)
print MapSqrt(L)
print ListSqrt(L)

         
