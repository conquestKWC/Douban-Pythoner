# -*- coding: cp936 -*-
#point:
#	1.model has a attribute __dict__
#	2.model can use getattr(model,attr)
#	3.verbose's meaning 
#
#
verbose = 1 #详情开关

def listing(model):
	if verbose:
		print '-'*30
		print 'name:'+model.__name__+'\nfile:'+model.__file__
		print '-'*30
	
	count = 0
	for x in model.__dict__.keys():
		print "%02d) %s"%(count, x),
		if x[0:2]=='__':
			print "<build-in name>"
		else:
			print model.__dict__[x]
		count+=1
	
	if verbose:
		print '-'*30
		print model.__name__,'has %d names'%(count)
		print '-'*30
	
if __name__=='__main__':
	import mydir
	listing(mydir)
