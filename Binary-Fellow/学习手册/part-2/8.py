# -*- coding: cp936 -*-
from echo import echo
echo(__file__)

S = 'spam'
ls = list(S)

try:
   print s[0][0][0][0][0]
except:
   print "ERROR"
#索引表达式？列表仍然可以像字符串一样用索引表达式
print ls[:3],S[:]
