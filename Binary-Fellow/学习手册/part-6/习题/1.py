#class adder
class Adder:
	def __init__(self, other):
		self.data = other
	def add(self, y):
		print 	"Not Implemented"
	def __add__(self, y ):
		return self.add( y.data )

class ListAdder(Adder):
	def add(self, y):
		temp = self.data[:]
		for i in y:
			temp.append(i)
		return temp

class DictAdder(Adder):
	def add(self, y):
		temp = self.data
		temp_keys = temp.keys()
		for i in y.keys():
			if i not in temp_keys:
				temp[i] = y[i]
		return temp

l1 = [1,2,3,4,5,6]
l2 = [2,3,4,5,6,7]
d1 ={ 'a':1,'b':2,'c':3}
d2 ={ 'd':4,'e':5,'f':6}
K = ListAdder(l1)
E = ListAdder(l2)
W = DictAdder(d1)
C = DictAdder(d2)

