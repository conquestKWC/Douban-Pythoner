def minmax( test , *args ):
   res = args[0]
   for arg in args[1:]:
      if test(arg,res):
         res = arg
   return res

def lessthan(x, y): return x < y
def grtrthan(x, y): return x > y


   
