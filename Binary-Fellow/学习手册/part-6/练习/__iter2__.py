# -*- coding: cp936 -*-
#���ظ������ĵ�������
#�����ǽ�__iter__��next����
'''
ÿһ�ε�������������SkipIteration
SkipObject __iter__
SkipIteration __init__
'''

class SkipObject:
   def __init__(self, wrapper):
      print "SkipObject __init__"
      self.wrapper = wrapper
   def __iter__(self):
      print "SkipObject __iter__"
      return SkipIteration(self.wrapper)

class SkipIteration:
   def __init__(self,wrapper):
      print "SkipIteration __init__"
      self.wrapper = wrapper
      self.offset = 0
   def next(self):
      if self.offset >= len(self.wrapper):
         print "StopIteration"
         raise StopIteration
      else:
         print "SkipIteration next"
         item = self.wrapper[self.offset]
         self.offset+=1
         return item

if __name__ == '__main__':
   chars = 'kewenchi'
   x = SkipObject(chars)
   for i in x:
      for j in x:
         print i+j,
      
