# -*- coding: cp936 -*-
from echo import echo
echo(__file__)

S = 'spam'

print S[:1]+'l'+S[2:]

#索引赋值不行，string是不可变对象
try:
   S[1] ='l'
except:
   print 'ERROR'
