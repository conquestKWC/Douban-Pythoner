
l = [1,2,3,4,5]
fp = open("part2-test.txt","w+")
#
try:
   print>>fp, "L[-1000:1000] = "+str(l[-100:100])
except:
   print>>fp, "Some trackback happend"
#
try:
   print>>fp, "L[4]="+str(l[5])
except:
   print>>fp, "Some trackback happend" 
#
try:
   print>>fp, l[3:1]
except:
   print>>fp, "Some trackback happend" 
#
try:
   l[645:1]=['x','y','z']
   print>>fp, "L = "+str(l)
except:
   print>>fp, "Some trackback happend"
fp.close()




