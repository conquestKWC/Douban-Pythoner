# -*- coding: cp936 -*-
#���ļ����룬��ӡ��stdout��

def echo(file):
   fp = open(file)
   temp = ''
   for line in fp:
      temp+=line
   print temp
   print '-'*30
   fp.close()
   

      
         
   
