# -*- coding: cp936 -*-
#可重复迭代的迭代对象
#核心是将__iter__与next分离
'''
每一次迭代，都会重置SkipIteration
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
      
