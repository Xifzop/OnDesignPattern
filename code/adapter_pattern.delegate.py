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

class Adapter(TextProcessor):

	def __init__(self, processor):
		self.tokenizer = processor

	def tokenize(self, source):
		return self.tokenizer.divide_words(source)

if __name__ == '__main__':
	adapter = Adapter(OutsideTokenizer())
	print adapter.tokenize('foo.bar.foo.bar.')