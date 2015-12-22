# -*- coding: cp936 -*-
#for
s = 'spam'
ls = list(s)

for x in xrange(len(ls)):
      ls[x]=ord(ls[x])
print ls

#修改
ls = list(s)

count =0
for x in xrange(len(ls)):
      count+=ord(ls[x])
print count

#map/reduce
temp = map(ord,s)
print temp
count = 0
count = reduce(lambda x,y:x+y,temp)


