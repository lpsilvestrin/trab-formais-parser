class Scanner:
	'reads the characteres from input source'

	def __init__(self, source):
		self.source = source
		self.file = open(source)

	def getChar(self):
		return self.file.read(1)
		
	def goBack(self):
		self.file.seek(-1, 1)