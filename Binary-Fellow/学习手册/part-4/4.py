# -*- coding: cp936 -*-
def adder(good, bad, ugly):
   return good+bad+ugly

#通用化
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

#其实不大好，这个假设是基于只传入一个字典
#的情况，没有考虑多个字典（到底会不会传入多个字典！？）
d = {'a':1,'b':2,'c':3}
      
