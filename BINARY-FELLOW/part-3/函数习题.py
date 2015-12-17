import sys

temp = sys.stdout
fp = open('function_test.txt','w+')
sys.stdout = fp

def func1():
   print X

def func2():
   X = 'NI!'

def func3():
   X = 'NI'
   print X

def func4():
   global X
   X = 'NI'

def func5():
   X = 'NI'
   def nested():
      print X
   nested()

X = 'Spam'
print 'Q%1>>>>>>>>'
func1()
print X
del X

X = 'Spam'
print 'Q%2>>>>>>>>'
func2()
print X
del X

X = 'Spam'
print 'Q%3>>>>>>>>'
func3()
print X
del X

X = 'Spam'
print 'Q%4>>>>>>>>'
func4()
print X
del X

X = 'Spam'
print 'Q%5>>>>>>>>'
func5()
print X
del X

fp.close()
sys.stdout = temp
