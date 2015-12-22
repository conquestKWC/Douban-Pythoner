from echo import echo
echo(__file__)

l = [1,2,3,4]
l[2] = []
print l

l = [1,2,3,4]
l[2:3] = []
print l

l = [1,2,3,4]
del l[2]
print l

l = [1,2,3,4]
del l[1:]
print l

l = [1,2,3,4]
try:
   l[1:2] = 1
   print l
except:
   print "SOME ERROR"

