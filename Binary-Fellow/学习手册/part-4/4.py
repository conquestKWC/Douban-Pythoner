# -*- coding: cp936 -*-
def adder(good, bad, ugly):
   return good+bad+ugly

#ͨ�û�
def adder_u(*argv):
   temp = []
   if type(argv[0]) != dict:
      temp.append(argv[0])
      for x in argv[1:]:
         temp[0]+=x
      return temp[0]
   else:
      tup = argv[0]
      key = argv[0].keys()
      temp = []
      temp.append(tup[key[0]])
      for x in key[1:]:
         temp[0]+=tup[x]
      return temp[0]

#��ʵ����ã���������ǻ���ֻ����һ���ֵ�
#�������û�п��Ƕ���ֵ䣨���׻᲻�ᴫ�����ֵ䣡����
d = {'a':1,'b':2,'c':3}
      
