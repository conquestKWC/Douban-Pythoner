# -*- coding: cp936 -*-
#__call__
print "#__call__"
import myrepr

class tcall(myrepr.test):
   def __call__(self,other):
      return self.number * other

x = tcall()
print x
print 'x(4) = ',x(4)

#���ں�����__call__

print "\n���ں�����__call__"
def callTest1(x):
   return 'callTest1',x*x

def callTest2(x):
   return 'callTest2',x+x

if __name__ == '__main__':
   print '''
   def callTest1(x):
      return 'callTest1',x*x

   def callTest2(x):
      return 'callTest2',x+x
      '''
   print "callTest1(12)",callTest1(12)
   print "callTest2(12)",callTest2(12)
   print "callTest1,callTest2 = callTest2.__call__,callTest1.__call__"
   callTest1,callTest2 = callTest2.__call__,callTest1.__call__
   print "callTest1(12)",callTest1(12)
   print "callTest2(12)",callTest2(12)

#���Կ�����python�ﺯ�������ķ�ʽ������ĺ���֮���Բ�ͬ����Ϊ__call__��ڵ�ַ�Ĳ�ͬ
   #���������__call__(����һ��mark,�κο��ñ�����),��ô�����ܹ�����Ϊһ������
#�����Դ󵨲²⣬python��һ�п��ܶ����࣬��һ�����������ɣ���Ϊ����Ҳ���̶ܹ���һ��
   #ȷ���ĵ�ַ����ڱ�����__call__�ϣ���ô���԰Ѻ�������һ�������ֻ��__call__
   #���Ե���
