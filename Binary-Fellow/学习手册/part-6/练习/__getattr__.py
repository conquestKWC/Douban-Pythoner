# -*- coding: cp936 -*-
#__getattr__���Ϊ��
#������ʵ���в����ڵĲ��֣�__getattr__�ͻᴥ��ȥ����Ƿ���__getattr__�еĶ���ķ���
#�����׳�AttributeError
#ע�����£�
#     1.getattr���ڻᴥ��AttributeErrorʱ��ȥ����Ƿ��壬����AttributeError
#     2.getattr����Ӱ�츳ֵ��������Ѿ���ֵ���ڵ����ݲ����κ�Ӱ��
#     3.getattr���ڲ�����attrbuteʱ�Żᴥ�������Ե���������ageһ������֮����������һ��ֵ��
#     ����ȥ����getattr
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
