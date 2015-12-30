# -*- coding: cp936 -*-
#__call__
print "#__call__"
import myrepr

class tcall(myrepr.test):
   def __call__(self,other):
      return self.number * other

x = tcall()
print x
print 'x(4) = ',x(4)

#关于函数的__call__

print "\n关于函数的__call__"
def callTest1(x):
   return 'callTest1',x*x

def callTest2(x):
   return 'callTest2',x+x

if __name__ == '__main__':
   print '''
   def callTest1(x):
      return 'callTest1',x*x

   def callTest2(x):
      return 'callTest2',x+x
      '''
   print "callTest1(12)",callTest1(12)
   print "callTest2(12)",callTest2(12)
   print "callTest1,callTest2 = callTest2.__call__,callTest1.__call__"
   callTest1,callTest2 = callTest2.__call__,callTest1.__call__
   print "callTest1(12)",callTest1(12)
   print "callTest2(12)",callTest2(12)

#可以看出，python里函数工作的方式，定义的函数之所以不同是因为__call__入口地址的不同
   #如果定义了__call__(对于一个mark,任何可用变量名),那么它就能够被视为一个函数
#更可以大胆猜测，python中一切可能都是类，由一个基类来生成，因为函数也不能固定到一个
   #确定的地址，入口被绑到了__call__上，那么可以把函数看作一个特殊的只有__call__
   #属性的类
