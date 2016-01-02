class MyList(list):
	def __init__(self, x = []):
		self.list = []
		for i in x:
			self.list.append(i)
	'''def __init__(self,x = []):
		if type(x) == list:
			self.list = x
		初始化应该独立出来，初始化出的类应该自己保留一份拷贝
		不要直接将用来初始化的值直接赋给类成员，一旦将来发生变化，且为
		可变变量，会使得生成的类中保存的值也跟着变化
	'''
#模拟list
	def __len__(self):
		return len(self.list)
	def __getitem__(self, key):
		return self.list[key]
	def __setitem__(self, key, value):
		self.list[key] = value
	def __delitem__(self, key):
		del self.list[key]
	def __getslice__(self, i, j):
		return MyList(self.list[i:j])
	def __setslice__(self, i, j, value):
		self.list[i:j] = value
	def __delslice__(self, i, j):
		del self.list[i:j]
		
	def __add__(self, x):
		'''(MyList+list/MyList+Mylist) all are avaliable'''
		try:
			if type(x) == type(self):
				temp = MyList(self.list+x.list)
				return temp
			elif type(x) == list:
				temp = MyList(self.list+x)
				return temp
			else:
				raise TypeError
		except TypeError:
			print "TypeError"
	def __radd__(self, x):
		try:
			if type(x) == type(self):
				temp = MyList(self.list+x.list)
				return temp
			elif type(x) == list:
				temp = MyList(self.list+x)
				return temp
			else:
				raise TypeError
		except TypeError:
			print "TypeError"
	def append(self, x):
		self.list.append(x)
	def __getattr__(self, attrname):
		print attrname
		return getattr(self.list,attrname)		
	def __iter__(self):
		return Skipiter(self.list)
	def __repr__(self):
		return str(self.list)
#?????ζ???????????		
class Skipiter:
	def __init__(self,x):
		self.wrapper = x
		self.offset = 0
	def next(self):
		if self.offset >= len(self.wrapper):
			raise StopIteration
		else:
			item = self.wrapper[self.offset]
			self.offset+=1
		return item

l1 = [1,2,3,4,5,6]
l2 = [2,3,4,5,6,7]
K = MyList(l1)
E = MyList(l2)

'''
a.（将list可变不可变分割开，当需要原处改变的时候直接赋值
	不需要原处改变时，用拷贝初始值）错误
	
	使用append的附件，不使用分片
	如果传入的是一个字符串序列，
	那个通过分片赋值的就是一个字符串而不是一个序列！
	会表现出不是列表的一些属性
	
b.可以，将(__getitem__\__setitem__\__delitem__\)
		   __getslice__\__setslice__\__delslice__全部重载，可以模拟序列操作
		   详细请看evernote中内置函数重载那个剪辑
c.可以，用__getattr__截取attrname，再用getattr(classname,attrname)
	效果如同classname.attrname,即将列表的方法调用到了包装的列表当中
	（委托）
d.1.可以 2.可以
	1.对加的变量进行检测，同型变量直接取LIST相加,
		非同型变量，检测是否为list
		MyList+MyList和MyList+list可加(定义__radd__实现左加，__add__实现右加)
		否则则抛出TypeError
	2.定义__radd__实现左加，__add__实现右加
e. 应该返回MyList类型，索引操作取单个返回孤立元素，取字串返回MyList
f.个人觉得嵌入一个更简单
	原因：通过委托的方式，可以将不必要重载的统统交给内嵌的list处理
		通过继承，必须修改一些内置函数才能正常工作
'''
