# -*- coding: cp936 -*-
#将文件读入，打印到stdout上

def echo(file):
   fp = open(file)
   temp = ''
   for line in fp:
      temp+=line
   print temp
   print '-'*30
   fp.close()
   

      
         
   
