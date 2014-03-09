#! /usr/bin/env python

from util import *

class BodyArmor(object):
	
	def __init__(self):
		self.id = "Armored."

class EnhancedBodyArmor(BodyArmor):
	
	def __init__(self):
		super(EnhancedBodyArmor, self).__init__()
		self.id = "Enhanced." + self.id

class NormalBodyArmor(BodyArmor):
	
	def __init__(self):
		super(NormalBodyArmor, self).__init__()
		self.id = "Normal." + self.id


class Weapon(object):
	@method_not_implemented
	def attack(self):
		pass

class SniperRifle(Weapon):
	
	def attack(self):
		print "shot and done!"

class DesertEagle(Weapon):

	def attack(self):
		print "Counterattack!"

# the abstract factory
class Factory:
	@method_not_implemented
	def produce_weapon(self):
		pass

	@method_not_implemented
	def produce_body_armor(self):
		pass

class KillerEquipFactory(Factory):

	def produce_weapon(self):
		return SniperRifle()

	def produce_body_armor(self):
		return EnhancedBodyArmor()

class SpyEquipFactory(Factory):

	def produce_weapon(self):
		return DesertEagle()

	def produce_body_armor(self):
		return NormalBodyArmor()

if __name__ == '__main__':
	killer_factory = KillerEquipFactory()
	spy_factory    = SpyEquipFactory()

	killer_kit = ( killer_factory.produce_weapon(), killer_factory.produce_body_armor() )
	spy_kit    = ( spy_factory.produce_weapon(), spy_factory.produce_body_armor() )

	print killer_kit, "\n", spy_kit