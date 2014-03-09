#! /usr/bin/env python

class Singleton(type):   
    def __init__(cls, name, bases, attr):
    	super(Singleton, cls).__init__(name, bases, dict)   
        cls._instance = None   
    def __call__(cls, *args, **kw):   
        if cls._instance is None:   
            cls._instance = super(Singleton, cls).__call__(*args, **kw)   
        return cls._instance


class WeaponManageDep(object):

	__metaclass__ = Singleton

	from datetime import datetime
	t = datetime

	def __init__(self):
		self.records = {}

	def log(self, agent_name):
		if not agent_name in self.records:
			self.records[agent_name] = self.__class__.t.now()
			print "Agent[%s] fetch his weapons at %s" % (agent_name, self.records[agent_name])
		else:
			print "Agent[%s] has already fetched his own weapons, no more." % agent_name

class WeaponManageDep(object):

	__metaclass__ = Singleton

	from datetime import datetime
	t = datetime

	def __init__(self):
		self.records = {}

	def log(self, agent_name):
		if not agent_name in self.records:
			self.records[agent_name] = self.__class__.t.now()
			print "Agent[%s] fetch his weapons at %s" % (agent_name, self.records[agent_name])
		else:
			print "Agent[%s] has already fetched his own weapons, no more." % agent_name

   

if __name__ == '__main__':
	dep_a = WeaponManageDep()
	dep_b = WeaponManageDep()

	dep_a.log('agentK')
	dep_b.log('agentK')

