# -*- coding: cp936 -*-
from echo import echo
echo(__file__)

l =[1,2,3,4]
t = (1,2,3,4)
s = '1234'
#a.+连接，连接字符串，序列，元组
print l+l[2:], t+t[2:], s[:2]+s[1:]

#b.当时字典时不能工作
d = { 'a':1,'b':2,'c':3 }
try:
   print d + d
except:
   print "ERROR"
#c.append能用于列表，不能用于字符串
try:
   l.append('1')
   print l,t,s
except:
   print "ERROR"
try:
   t.append('1')
   print l,t,s
except:
   print "ERROR"
#d 列表还是列表，字符串还是字符串
l = l[2:]+l[:]
print (type(l))
s = s[1:]+s[:3]
print (type(s))
   
