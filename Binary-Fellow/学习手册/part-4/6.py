# -*- coding: cp936 -*-
from echo import echo
echo(__file__)
from test import *
#�Ӳ���ģ����������ֵ䣬��ӡ��������

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
         #��ΪԪ��������ԣ�������ԭ���޸ģ�ֻ�ܽ������б����ת��ΪԪ��
         temp = list(two)
         for x in one:
            if x not in two:
               temp.append(x)
         return tuple(temp)
      else:
         return two+one#�������ֵ����
   else:
      print "can't add two different type"

print addict(d1,d1)
#��ͨ�û�
try:
   print addict(l1,l2)
except:
   print "out range of index"
#ͨ�û�
print add_u(l1,l2),add_u(t2,t1),add_u(s1,s2),add_u(d1,d2)
