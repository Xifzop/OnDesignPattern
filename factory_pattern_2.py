#! /usr/bin/env python

from util import *

class Agent:
	@method_not_implemented
	def do_task(self, msg):
		pass

class KillerAgent(Agent):

	def __init__(self):
		self.id = "I'm a killer."

	def do_task(self, msg):
		print "Get task: target to kill >", msg, "."

class SpyAgent(Agent):

	def __init__(self):
		self.id = "I'm a spy."

	def do_task(self, msg):
		print "Get task: target to steal >", msg, "."

class AgentFactory:

	def train_killer_agent(self):
		return KillerAgent()

	def train_spy_agent(self):
		return SpyAgent()

'''
	test multi-factory method.
'''
if __name__ == '__main__':
	agent_factory = AgentFactory()
	killer = agent_factory.train_killer_agent()
	spy    = agent_factory.train_spy_agent()

	killer.do_task('Bill')
	spy.do_task('bill')