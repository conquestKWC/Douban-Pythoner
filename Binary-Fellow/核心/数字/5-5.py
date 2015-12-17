
L = [25,10,5,1]
count = [0,0,0,0]

def GetCent():
   while True:
      print "Input $(0-100cent)"
      try:
         cent = int(raw_input())
         if -1<cent<101:
            break
         else:
            print "ERROR INPUT(0-100)"
      except:
         print "Try again"
   return cent

cent = GetCent()
i = 0
while cent:
   count[i] = cent/L[i]
   cent%=L[i]
   i+=1

print "25*%d+10*%d+5*%d+1*%d=%d"%(count[0],count[1],count[2],
                                  count[3],25*count[0]+10*count[1]
                                  +5*count[2]+count[3])
      

