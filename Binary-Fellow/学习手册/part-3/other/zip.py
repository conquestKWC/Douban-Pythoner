# -*- coding: cp936 -*-
def GetPersonInfo():
   Info = ('name', 'age', 'phone number', 'profession', 'Address', 'mail')
   name = str(raw_input('Your name : e.x:XXX(first) XX(mid) XXX:'))
   name = name.split(' ');
   age = int(raw_input('Age is :'))
   Address = str(raw_input('Address is :'))
   job = str(raw_input('Profession is :'))
   phone = str(raw_input('Phone number is:'))
   mail = str(raw_input('Email is :'))
   detail = (name,age,phone,job,Address,mail)
   L = []
##############
   L = zip(Info,detail)#zip�÷�
   #��Info��detail�ĵ���Ԫ����ϳ�һ��tuple���ǳ�����ת��Ϊ�ֵ䣩
##############
   return L  #����һ���б�ֱ�ӿ�����dictת��Ϊ�ֵ�

detail = GetPersonInfo()
PersonInfo = dict(detail)



