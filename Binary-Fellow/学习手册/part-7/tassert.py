# -*- coding: cp936 -*-
#assert ��<test>Ϊ��ʱ�������ã���<test>Ϊ��ʱ��������
#����������ֵ�ļ���
#������֤����������ֵ�Ƿ�Ϊ����ֵ��<test>Ϊ�棩��һ��Ϊ������ֵ��<test>����Ϊ�٣�

#�ռ��û����������

def f(x):
   assert x < 0, ' x must a negative'
   return x ** 2

print "f(-1 ):",f(-1)
print "\nf( 1 ):",f(1)
