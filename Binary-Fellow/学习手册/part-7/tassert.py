# -*- coding: cp936 -*-
#assert 当<test>为真时不起作用，当<test>为假时，起作用
#可用于允许值的检验
#用来验证程序运行中值是否为允许值（<test>为真），一旦为非允许值（<test>部分为假）

#收集用户定义的条件

def f(x):
   assert x < 0, ' x must a negative'
   return x ** 2

print "f(-1 ):",f(-1)
print "\nf( 1 ):",f(1)
