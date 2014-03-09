
#decorator for unimplemented method to simulate the interface in Java
def not_implemented(t):
	def unimplemented_notify(self):
		raise Exception(t + ' Not Implemented.')
	return unimplemented_notify

def method_not_implemented(method):
	return not_implemented('method')