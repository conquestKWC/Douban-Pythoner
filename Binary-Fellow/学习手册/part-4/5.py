# -*- coding: cp936 -*-
from echo import echo
echo(__file__)

#����һ���ֵ䣬���ֵ��ÿ��Ԫ�ظ�ֵ
def copydict(Dict):
   temp = {}
   if type(Dict) == dict:
      for x in Dict:#�����ֵ�ļ�ֵ
         temp[x] = 0#��ֵ����
   return temp
#����һ�����ֵ䣬���ı�ԭ�ֵ�

d = {'a':123,'b':234,'c':345,'d':456}

#����������d[:]���㸴�ƣ����Ͳ�����
#1)
print copydict(d)
#2)
try:
   temp = d[:]
   print temp
except:
   print "Error"
