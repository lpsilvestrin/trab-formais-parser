from lexical_rules import *
from token import Token

class Parser:
	def __init__(self, tokenList):
		self.tokenList = tokenList
		self.pos = 0

	def getToken(self):
		return self.tokenList[self.pos]

	def parse(self):
		if self.program():
			return True
		return False

	def program(self):
		if self.codeBlock("eof", False):
			return True
		elif self.functionDef():
			self.pos+=1
			if self.program():
				return True

	def boolTest(self):
		if self.expression():
			self.pos += 1
			self.getToken().text
			if self.getToken().type == COMPARATOR:
				self.pos += 1
				if self.expression():
					return True
		return False

	def functionDef(self):
		pos = self.pos
		if self.getToken().text == "def":
			self.pos+= 1
			if self.getToken().type == IDENTIFIER:	
				self.pos+= 1
				if self.getToken().text == "(":
					self.pos+=1
					if self.parametersDef():	
						self.pos+= 1
						if self.getToken().text == "{":
							self.pos+= 1
							if self.codeBlock("}", True):
								return True
		self.pos = pos
		return False

	def assignment(self):
		if self.getToken().type == IDENTIFIER:
			self.pos+= 1
			if self.getToken().text == "=":
				self.pos+= 1
				if self.expressionChain() or self.expression():
					return True
		return False

	def expression(self):
		if self.functionCall() or self.getToken().type == IDENTIFIER or self.getToken().type == NUMBER:
			return True
		return False

	def expressionChain(self):
		pos = self.pos
		if self.expression():
			self.pos+=1
			if self.expressionRest():
				return True
		self.pos = pos
		return False

	def expressionRest(self):
		if self.getToken().text == ";":
			return True
		elif self.getToken().text in OPERATORS:
			self.pos += 1
			if self.expression():
				self.pos+=1
				if self.expressionRest():
					return True
		return False

	def functionCall(self):
		pos = self.pos
		if self.getToken().type == IDENTIFIER:
			self.pos+=1
			if self.getToken().text == "(":
				self.pos+=1
				if self.parameters():
					return True
		self.pos = pos
		return False

	def parametersDef(self):
		pos = self.pos
		if self.getToken().type == IDENTIFIER:
			self.pos+=1
			if self.parametersDefRest():
				return True
		self.pos = pos
		return False

	def parametersDefRest(self):
		pos = self.pos
		if self.getToken().text == ")":
			return True
		elif self.getToken().text == ",":
			self.pos+=1
			if self.getToken().type == IDENTIFIER:
				self.pos+=1
				if self.parametersDefRest():
					return True
		self.pos = pos
		return False

	def parameters(self):
		pos = self.pos
		if self.getToken().type == IDENTIFIER or self.getToken().type == NUMBER:
			self.pos+=1
			if self.parametersRest():
				return True
		self.pos = pos
		return False

	def parametersRest(self):
		pos = self.pos
		if self.getToken().text == ")":
			return True
		elif self.getToken().text == ",":
			self.pos+=1
			if self.getToken().type == IDENTIFIER or self.getToken().type == NUMBER:
				self.pos+=1
				if self.parametersRest():
					return True
		self.pos = pos
		return False

	def codeLine(self, hasReturn):
		pos = self.pos
		if self.assignment():
			return True
		self.pos = pos
		if self.functionCall():
			self.pos+=1
			if self.getToken().text == ";":
				return True
		if hasReturn:
			if self.functionReturn():
				return True
		self.pos = pos
		return False

	def codeBlock(self, endTok, hasReturn):
		pos = self.pos
		if self.getToken().text == endTok:
			return True
		elif self.codeLine(hasReturn):
			self.pos+=1
			if self.codeBlock(endTok, hasReturn):
				return True
		elif self.whileIf(hasReturn):
			self.pos+=1
			if self.codeBlock(endTok, hasReturn):
				return True
		self.pos = pos
		return False

	def whileIf(self, hasReturn):
		pos = self.pos
		if self.getToken().text == "while" or self.getToken().text == "if":
			self.pos+=1
			if self.getToken().text == "(":
				self.pos+=1
				if self.boolTest():
					self.pos+=1
					if self.getToken().text == ")":
						self.pos+=1
						if self.getToken().text == "{":
							self.pos+=1
							if self.codeBlock("}", hasReturn):
								return True
		self.pos = pos
		return False

	def functionReturn(self):
		if self.getToken().text == "return":
			self.pos+=1
			if self.expression():
				self.pos+=1
				if self.getToken().text == ";":
					return True
		return False