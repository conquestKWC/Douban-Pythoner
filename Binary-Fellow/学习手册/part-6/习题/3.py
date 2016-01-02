from mymodel import MyList

class MyListSub(MyList):
	times = 0
	def __init__(self, x = []):
		MyList.__init__(self,x)
		MyListSub.times+=1
		self.calltimes = 0
	def __getattr__(self, attrname):
		self.calltimes+=1
		print "call %s calltimes %d"%(attrname, self.calltimes)
		return MyList.__getattr__(self, attrname)
		
if __name__=='__main__':
	K = MyListSub([1,2,3,4])
	E = MyListSub()
	for x in xrange(10):
		K.append( x )
	for x in xrange(8):
		E.append( x )	
	print K,E 
	
