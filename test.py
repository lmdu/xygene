class route:
	def __init__(self, path, name):
		self.path = path
		#print name
		#print path

	def __call__(self, cls):
		print cls
		return str

@route('/', name="abc")
class test:
	def __init__(self):
		pass

if __name__ == '__main__':
	test()