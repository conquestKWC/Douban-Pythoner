# -*- coding: cp936 -*-
#元组赋值运算
#  交换两个变量最好用这种方法
#  x, y = y, 
#
from echo import echo
echo(__file__)

X = 'spam'
Y = 'eggs'
print 'change:'+X,Y
X, Y = Y, X
print 'changed:'+X,Y
