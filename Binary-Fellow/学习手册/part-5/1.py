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

#设置缓冲区
def countChars1(name):
   try:
      fp = open(name)
   except:
      print "Can't open this file"
      return
   count = 0
   for x in fp:    #以行为缓冲
      count+=len(x)
   return count

#不设缓冲区
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

