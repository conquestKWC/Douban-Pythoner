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
   L = zip(Info,detail)#zip用法
   #将Info与detail的单个元素组合成一个tuple（非常方便转换为字典）
##############
   return L  #返回一个列表，直接可以用dict转换为字典

detail = GetPersonInfo()
PersonInfo = dict(detail)



