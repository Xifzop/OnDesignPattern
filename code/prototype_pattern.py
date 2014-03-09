#! /usr/bin/env python

from util import *

class RobotPrototype(object):

	@method_not_implemented
	def clone(self):
		pass

class Engine(object):
	
	def __init__(self):
		print "Constructing engine.."
		print "It may take large amounts of time to initialize the resource.."

class AssistRobotPrototype(RobotPrototype):

	def __init__(self, engine=None):
		if engine is None:
			self.engine = Engine()
		else:
			self.engine = engine
		import random as rnd
		self.id = rnd.randint(1,100)

	# Deep clone..
	def clone(self):
		new_instance = self.__class__.__new__(self.__class__)
		new_instance.engine = self.engine
		new_instance.id     = self.id
		return new_instance

	def simple_clone(self):
		new_instance = self.__class__.__new__(self.__class__)
		new_instance.engine = Engine()
		new_instance.id     = self.id
		return new_instance


if __name__ == '__main__':
	# test for deep clone..
	robot_a = AssistRobotPrototype()
	robot_b = robot_a.clone()
	print robot_a.engine == robot_b.engine
	print robot_b.id, robot_a.id

	# test for simple clone..
	robot_c = robot_a.simple_clone()
	print robot_a.id, robot_c.id
	print robot_a.engine == robot_c.engine
