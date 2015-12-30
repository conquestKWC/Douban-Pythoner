# -*- coding: cp936 -*-
#һ�ζԵ���Э���̽��
#��һ���ɵ���������е�������һ����ҪȥѰ�ҿɵ�����־__iter__
#��__iter__һͬ����Ӧ�û���next
#��һ�ε���__iter__Ȼ���ٵ���nextֱ��raise StopIteration


#����__iter__���
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

#��__iter__
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
   


      
