# -*- coding: cp936 -*-
#�ֵ���������
#

from echo import echo
echo(__file__)

D = {'a':1,'b':2,'c':3}

#��ͼ���������ڵļ�ֵ���ᱨ��
try:
   print D['d']
except:
   print "SOME ERROR"

#�Բ����ڵ�������ֵ�������¼�
try:
   D['d'] = 'spam'
   print D
except:
   print "SOME ERROR"

#�б��ܶԱ߽������ֵ���и�ֵ
l = [1,2,3]
try:
   l[5] = 23
   print l
except:
   print "SOME ERROR"




