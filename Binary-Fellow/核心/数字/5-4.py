def judge(a):
   return (( a%4==0 and a%100!=0) or( a%400==0))

def GetYear():
   year = 0
   while not year:
      try:
         print "Input a year"
         year = int(raw_input())
         if year is int:break
      except:
         print "Iligal input.Try again"
   return year

if judge(GetYear()):
   print "Y"
else:
   print "N"
      
   
