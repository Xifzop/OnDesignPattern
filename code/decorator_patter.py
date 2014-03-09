#! /usr/bin/env python

from functools import wraps

def memoize(func):
    cache = {}
    print "in mem:", cache

    @wraps(func)
    def wrapper(*args):
        if args not in cache:
        	print "put into "
        	cache[args] = func(*args)
		return cache[args]

    return wrapper

@memoize
def an_expensive_function(arg1, arg2, arg3):
	print arg1, arg2, arg3


an_expensive_function(1,2,3)


class A(object):

	def __init__(self):
		self.id = "d"

	def __getattr__(self, name):
		print self, name
		return 0

	
	def __getattribute__(self, name):
		print self, name
		return 1


print A().id
print A().name