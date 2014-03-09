#! /usr/bin/env python

from util import *

class TextProcessor(object):

	@method_not_implemented
	def tokenize(self, source):
		pass

	# ... ... some other methods

class OutsideTokenizer(object):

	def divide_words(self, source):
		results = []
		results = source.split('.')
		# some other operations ...
		return results

class Adapter(TextProcessor, OutsideTokenizer):
	def tokenize(self, source):
		return self.divide_words(source)

if __name__ == '__main__':
	sub_adapter = Adapter()
	print sub_adapter.tokenize('foo.bar.foo.bar.')

