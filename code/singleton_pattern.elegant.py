#! /usr/bin/env python

def singleton(cls, *args, **kw):
	instances = {}
	def _singleton():
		print instances
		if cls not in instances:
			instances[cls] = cls(*args, **kw)
		return instances[cls]
	return _singleton


@singleton
class WeaponManageDep(object):

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