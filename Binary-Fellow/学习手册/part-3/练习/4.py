# -*- coding: cp936 -*-
from echo import echo
echo(__file__)

L = [1,2,4,8,16,32,64]
X = 5

#开始
found = i = 0
while not found and i < len(L):
   if 2 ** X == L[i]:
      found = 1
   else:
      i = i+1
if found:
   print 'at index',i
else:
   print X, 'not found'

#a.重写
i = 0
temp = len(L)
while i < temp:
   if 2 ** X == L[i]:
      print 'at index',i
      break;
   else:
      i+=1
else:
   print 'No found'

#b.重写
temp = 2 ** X
for x in L:
   if temp == x:
      print 'at index',L.index(temp)
      break
else:
   print 'No found'
#c.重写
temp = 2 ** X
if temp in L:
   print 'at index',L.index(temp)
else:
   print 'No found'
#d.硬编码产生l
l = []
for i in range(7):
   l.append(2 ** i)
print l

#e.能改善，参见重写#c

#f.
lf = map(lambda x: 2 ** x,range(7))
print lf
