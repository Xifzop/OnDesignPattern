#! /usr/bin/env python


def deco(cls):  
    def _deco(func):  
        def __deco():  
            print("before %s called [%s]." % (func.__name__, cls))  
            cls.acquire()  
            try:  
                return func()  
            finally:  
                cls.release()  
        return __deco  
    return _deco  

class InitSingleton(object):

	@staticmethod
	def acquire():
		pass

	@staticmethod
	def release():
		pass

@deco(InitSingleton)
def test():
	print "test called."
