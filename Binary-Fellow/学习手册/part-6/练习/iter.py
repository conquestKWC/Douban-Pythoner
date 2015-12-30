# -*- coding: cp936 -*-
#一次对迭代协议的探究
#对一个可迭代对象进行迭代，第一步是要去寻找可迭代标志__iter__
#与__iter__一同出现应该还有next
#第一次调用__iter__然后再调用next直到raise StopIteration


#不含__iter__标记
class MSquar:
   def __init__(self, start, stop):
      print "call __init__"
      self.value = start-1
      self.stop = stop
   def mark(self):
      print "call __iter__"
      return self
   def next(self):
      print "call next"
      if self.value == self.stop:
         print "StopIteration"
         raise StopIteration
      self.value+=1
      return self.value ** 2

#含__iter__
class Squar:
   def __init__(self, start, stop):
      print "call __init__"
      self.value = start-1
      self.stop = stop
   def __iter__(self):
      print "call __iter__"
      return self
   def next(self):
      print "call next"
      if self.value == self.stop:
         print "StopIteration"
         raise StopIteration
      self.value+=1
      return self.value ** 2

if __name__ == '__main__':
   print "MSquar"
   x = MSquar(1,5)
   try:
      for i in x:print i
   except:
      print "Can't Iteration\n"
   print "Squar"
   y = Squar(1,5)
   for i in y:print i
   


      
