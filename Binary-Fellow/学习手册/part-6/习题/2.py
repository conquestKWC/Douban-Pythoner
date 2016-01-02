class MyList(list):
	def __init__(self, x = []):
		self.list = []
		for i in x:
			self.list.append(i)
	'''def __init__(self,x = []):
		if type(x) == list:
			self.list = x
		��ʼ��Ӧ�ö�����������ʼ��������Ӧ���Լ�����һ�ݿ���
		��Ҫֱ�ӽ�������ʼ����ֱֵ�Ӹ������Ա��һ�����������仯����Ϊ
		�ɱ��������ʹ�����ɵ����б����ֵҲ���ű仯
	'''
#ģ��list
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
#?????��???????????		
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
a.����list�ɱ䲻�ɱ�ָ������Ҫԭ���ı��ʱ��ֱ�Ӹ�ֵ
	����Ҫԭ���ı�ʱ���ÿ�����ʼֵ������
	
	ʹ��append�ĸ�������ʹ�÷�Ƭ
	����������һ���ַ������У�
	�Ǹ�ͨ����Ƭ��ֵ�ľ���һ���ַ���������һ�����У�
	����ֳ������б��һЩ����
	
b.���ԣ���(__getitem__\__setitem__\__delitem__\)
		   __getslice__\__setslice__\__delslice__ȫ�����أ�����ģ�����в���
		   ��ϸ�뿴evernote�����ú��������Ǹ�����
c.���ԣ���__getattr__��ȡattrname������getattr(classname,attrname)
	Ч����ͬclassname.attrname,�����б�ķ������õ��˰�װ���б���
	��ί�У�
d.1.���� 2.����
	1.�Լӵı������м�⣬ͬ�ͱ���ֱ��ȡLIST���,
		��ͬ�ͱ���������Ƿ�Ϊlist
		MyList+MyList��MyList+list�ɼ�(����__radd__ʵ����ӣ�__add__ʵ���Ҽ�)
		�������׳�TypeError
	2.����__radd__ʵ����ӣ�__add__ʵ���Ҽ�
e. Ӧ�÷���MyList���ͣ���������ȡ�������ع���Ԫ�أ�ȡ�ִ�����MyList
f.���˾���Ƕ��һ������
	ԭ��ͨ��ί�еķ�ʽ�����Խ�����Ҫ���ص�ͳͳ������Ƕ��list����
		ͨ���̳У������޸�һЩ���ú���������������
'''
