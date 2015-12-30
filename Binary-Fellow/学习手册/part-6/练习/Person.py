# -*- coding: cp936 -*-
#类代码编写细节

class GenericDisplay:
   def __str__(self):
      restr = '\n'+self.__class__.__name__ +':\n'
      for key in self.__dict__.keys():
         restr+=('\t'+str(key)+'='+str(self.__dict__[key])+'\n')
      return restr
   
class Person(GenericDisplay):
   def __init__(self, name = None, age = None, birth = None):
      if name != None:
         self.firstName = name.split()[0]
         self.secondName = name.split()[-1]
      self.birth = birth
      self.age = age
   def __repr__(self):
      return ("firstName: %s,secondName: %s\n"
              +"birth: %s")%(self.firstName, self.secondName,
                             self.birth)
   def setFirstName(self,fname):
      self.firstName = fname
   def setSecondName(self,sname):
      self.secondName = sname
   def setBirth(self,birth):
      self.birth = birth
   def setAge(self,age):
      self.age = age
      
   def getFirstName(self):
      return self.firstName
   def getSecondName(self):
      return self.secondName
   def getBirth(self):
      return self.birth
   def getAge(self):
      return self.age
   
class Employee(Person):
   def __init__(self, name = None, age = None, birth = None, salary = None, job = None):
      Person.__init__(self, name, age, birth)
      self.salary = salary
      self.job = job

   def setSalary(self,salary):
      self.salary = salary
   def setJob(self,job):
      self.job = job

   def getSalary(self):
      return self.salary
   def getJob(self):
      return self.job

   def giveRaise(self,precent):
      self.salary*=(precent+1)
   
if __name__ == '__main__':
   argv = {'name':'welch K','age':20,'job':'student','salary':1500,'birth':'21 May'}
   Ke = Employee(**argv)
   print '''
   argv = {'name':'welch K','age':20,'job':'student','salary':1500,'birth':'21 May'}
   Ke = Employee(**argv)
   print Ke'''
   print Ke
