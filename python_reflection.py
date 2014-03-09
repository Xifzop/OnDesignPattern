




def enhance_method(klass, method_name, replacement):
    method = getattr(klass, method_name)
    setattr(klass, method_name, new.instancemethod(
        lambda *args, **kwds: replacement(method, klass, *args, **kwds), None, klass))

def another(old, cls, self):
	print 'world'
	print old
	print self
	print cls
