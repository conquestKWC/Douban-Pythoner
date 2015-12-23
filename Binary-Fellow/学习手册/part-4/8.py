# -*- coding: cp936 -*-
def prime(a):
   if float == type(a) or int == type(a):
      if a-int(a) > 0.0000001:
         print "this float can't be see a integer"
         return 
      if a < 0:
         print "negetive integer is not prime"
         return None
   else:
      return None
   y = int(a)
   x = int(a/2)
   while x > 1:
      if y % x == 0:
         print a, 'has factor', x
         break
      x-=1
   else:
      print a, 'is prime'

#加快版？然而这个并不快
def qprime(a):
   if float == type(a) or int == type(a):
      if a-int(a) > 0.0000001:
         print "this float can't be see a integer"
         return 
      if a < 0:
         print "negetive integer is not prime"
         return 
   else:
      return None
   y = int(a)
   x = int(a/2)
   temp = [ i for i in range(x) if x%y==0 ]
   if temp == [ ]:
      print a, 'is prime'
   else:
      print a, 'has factor'
