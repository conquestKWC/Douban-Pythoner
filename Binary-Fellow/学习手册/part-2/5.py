# -*- coding: cp936 -*-
#����һ����a��ֵΪb ----- D[a] = b
#
from echo import echo
echo(__file__)

D = {}
D[1] = 'a'
D[2] = 'b'
print D
#������Ϊ��������

D[(1,2,3)] = 'c'
print D
