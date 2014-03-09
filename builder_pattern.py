#! /usr/bin/env python

#	wireless communication device may include componnents as follows:
#	sender_device, receive_device, mask	

from util import *

class Mask(list):
	
	def __iadd__(self, other):
		if type(other) is list:
			super(Mask, self).__add__(other)
		else:
			self.append(other)
		return self		

class SenderDev(object):
	pass

class ReceiveDev(object):
	pass

class SonyMask(Mask):
	pass

class SonySenderDev(SenderDev):
	pass

class SonyReceiveDev(ReceiveDev):
	pass

class Builder(object):

	@method_not_implemented
	def produce_sender_dev(self):
		pass

	@method_not_implemented
	def produce_receive_dev(self):
		pass

	@method_not_implemented
	def produce_mask(self):
		pass

class SonyBuilder(Builder):

	def produce_sender_dev(self):
		return SonySenderDev()

	def produce_receive_dev(self):
		return SonyReceiveDev()

	def produce_mask(self):
		return SonyMask()

class Director(object):

	def __init__(self, builder=None):
		self._builder = builder

	def direct_to_build(self):
		if self._builder is None:
			raise Exception("Builder Error.")
		else:
			mask = self._builder.produce_mask()
			receiver = self._builder.produce_receive_dev()
			sender   = self._builder.produce_sender_dev()
			mask += receiver
			mask += sender
		return mask

if __name__ == '__main__':
	sony_builder = SonyBuilder()
	director = Director(sony_builder)
	product = director.direct_to_build()
	print product
