# -*- coding: cp936 -*-
#�����ֵ�

d = {'h':1,'b':2,'c':3,'d':4}
#����sorted����
print sorted(d)
l = d.keys()
#keys������ȡ�ؼ����б���sort��������
l.sort()
print l

#���ؼ��ֺ�ֵת��Ϊһ��Ԫ�飬�����б�ld�У���ld��������ld����ֱ��ת��Ϊ�ֵ䣬ȡ��Ҳ�ܷ���
ld = []
for i in l:
   ld.append((i,d[i]))
ld.sort()
print ld

