#! /usr/bin/env python

from util import *

class TextProcessor(object):

	@method_not_implemented
	def tokenize(self, source):
		pass

	# ... ... some other methods

class OutsideTokenizer(object):

	def divide_words(self, source):
		source.split()
		# some other operations ...

class Adapter(TextProcessor, OutsideTokenizer):
	def tokenize(self, source):
		
