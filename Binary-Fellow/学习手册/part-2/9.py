# -*- coding: cp936 -*-
from echo import echo
echo(__file__)

S = 'spam'

print S[:1]+'l'+S[2:]

#������ֵ���У�string�ǲ��ɱ����
try:
   S[1] ='l'
except:
   print 'ERROR'
