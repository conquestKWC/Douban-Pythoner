# -*- coding: cp936 -*-

name = "test.txt"

def countLine(name):
   try:
      fp = open(name)
   except:
      print "Can't open this file"
      return
   count = 0
   for x in fp:
      count+=1
   return count

#���û�����
def countChars1(name):
   try:
      fp = open(name)
   except:
      print "Can't open this file"
      return
   count = 0
   for x in fp:    #����Ϊ����
      count+=len(x)
   return count

#���軺����
def countChars2(name):
   try:
      fp = open(name)
   except:
      print "Can't open this file"
      return
   count = 0
   for x in fp.read():
      count+=1
   return count

