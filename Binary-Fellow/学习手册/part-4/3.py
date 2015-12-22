def adder(*argv):
   count = None
   if str == type(argv[0]):
      count = ''
   elif (int == type(argv[0])) or ( float == type(argv[0])):
      count = 0
   elif list == type(argv[0]):
      count =[]
   else:
      count = ()
      
   for x in argv:
      count+=x
   return count

s = '1232'
l = [1,2,3]
t = (1,2,3,4)
print adder(t,t,t,t,t,t)
