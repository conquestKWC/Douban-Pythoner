# -*- coding: cp936 -*-
from echo import echo
echo(__file__)

S = 'spam'
ls = list(S)

try:
   print s[0][0][0][0][0]
except:
   print "ERROR"
#�������ʽ���б���Ȼ�������ַ���һ�����������ʽ
print ls[:3],S[:]
