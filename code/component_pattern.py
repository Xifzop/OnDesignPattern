#! /usr/bin/env python

from util import *

class CommentFilter(object):

	@method_not_implemented
	def process(self, msg):
		pass


class LeafFilter(CommentFilter):

	def __init__(self):
		super(TerminalFilter, self).__init__()

	def process(self, msg):
		print "Processing some data ... :", msg
		print "Then post to @#!$"

class NodeFilter(CommentFilter):

	def __init__(self):
		super(NodeFilter, self).__init__()
		self.childs = []

	@method_not_implemented
	def self_process(self, msg):
		pass

	def process(self, msg):
		output = self.self_process(msg)
		for child in self.childs:
			child.process(output)



