#! /usr/bin/env python

from util import *

class LazySingleton(object):

	def __new__(cls, *args, **kw):
		if not hasattr(cls, '_only_instance'):
			cls._only_instance = super(LazySingleton, cls).__new__(cls, *args, **kw)

		return cls._only_instance


class WeaponManageDep(LazySingleton):

	from datetime import datetime
	t = datetime

	def __init__(self):
		super(WeaponManageDep, self).__init__()
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