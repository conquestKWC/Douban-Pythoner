# -*- coding: cp936 -*-
#Ԫ�鸳ֵ����
#  ��������������������ַ���
#  x, y = y, 
#
from echo import echo
echo(__file__)

X = 'spam'
Y = 'eggs'
print 'change:'+X,Y
X, Y = Y, X
print 'changed:'+X,Y
