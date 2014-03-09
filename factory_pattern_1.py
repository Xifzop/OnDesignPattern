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

class DefaultAgent(Agent):

	def __init__(self):
		self.id = "I'm null type agent."

	def do_task(self, msg):
		print "Get task but do nothing, 'cause I'm null type Agent."


AgentCategories = {
	'killer' : KillerAgent,
	'spy'    : SpyAgent
}

class AgentFactory:
	#@staticmethod
	def train_agent(self, agent_type):
		if agent_type in AgentCategories:
			return AgentCategories[agent_type]()
		else:
			return DefaultAgent()

'''
	test for uni-factory pattern
'''
if __name__ == '__main__':
	agent_factory = AgentFactory()
	killer = agent_factory.train_agent('killer')
	spy    = agent_factory.train_agent('spy')
	anony  = agent_factory.train_agent('nonexist')

	killer.do_task('Bill')
	spy.do_task('bill')
	anony.do_task('do something')