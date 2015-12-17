def judge(grade):
   Grade = {-1:'F',9:'A',8:'B',7:'C',6:'D',10:'A'}
   try:
      return Grade[grade/10]
   except:
      return Grade[-1]

def GetGrade():
   while True:
      print "Input Grade(0-100)"
      try:
         grade = int(raw_input())
         if -1<grade<101:
            break
         else:
            print "ERROR INPUT(0-100)"
      except:
         print "Try again"
   return grade

a = GetGrade()
print 'Grade is:'+judge(a)
