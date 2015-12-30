#__repr__

class test:
   def __init__(self,number = 1,name = None):
      self.number = number
      self.name = name
   def __repr__(self):
      return "test number:%d,name:%s"%(self.number,self.name)

x = test()
print x
