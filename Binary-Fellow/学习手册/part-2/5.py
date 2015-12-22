# -*- coding: cp936 -*-
#生成一个键a，值为b ----- D[a] = b
#
from echo import echo
echo(__file__)

D = {}
D[1] = 'a'
D[2] = 'b'
print D
#键可以为任意类型

D[(1,2,3)] = 'c'
print D
