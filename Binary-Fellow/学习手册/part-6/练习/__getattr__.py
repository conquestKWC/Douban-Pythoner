# -*- coding: cp936 -*-
#__getattr__理解为：
#当引用实例中不存在的部分，__getattr__就会触发去检查是否是__getattr__中的定义的方法
#否则抛出AttributeError
#注意以下：
#     1.getattr仅在会触发AttributeError时先去检查是否定义，否则AttributeError
#     2.getattr不会影响赋值，不会对已经赋值存在的数据产生任何影响
#     3.getattr仅在不存在attrbute时才会触发，所以当下面类中age一旦定义之后，正常返回一个值，
#     不在去调用getattr
class empty:
   def __init__(self):
      self.value = 100
   def __getattr__(self, attrname):
      if attrname == 'age':
         print "__getattr__ age",
         return 40
      else:
         print "__getattr__",
         raise  AttributeError,attrname


if __name__=='__main__':
   x = empty()
   print "print x.age ",x.age
   print "print x.value ",x.value
   try:
      print x.name
   except:
      print "print x.name AttributeError"
   x.age = 123
   print "print x.age ",x.age
