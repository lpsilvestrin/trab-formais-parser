from scanner import Scanner
from lexical_rules import *
from token import Token

class Lexer:
	'identifies tokens from source file'

	def __init__(self, filename):
		self.filename = filename
		self.scanner = Scanner(filename)
		self.char = self.scanner.getChar()

	def getToken(self):
		word = ''

		# getting white spaces
		if self.char in WHITESPACE_CHARS:
			while self.char in WHITESPACE_CHARS:
				self.char = self.scanner.getChar()
			token = Token(word)
			token.type = "WHITESPACE"

		# EOF
		if self.char == '':
			token = Token("eof")
			token.type = "EOF"

		# getting comparator tokens
		elif self.char in COMPARATORS:
			token = Token(self.char)
			token.type = "COMPARATOR"
			self.char = self.scanner.getChar()

		# getting one-character tokens
		elif self.char in ONECHARSYMBOLS:
			token = Token(self.char)
			token.type = "ONECHARSYMBOL"
			self.char = self.scanner.getChar()

		# getting number tokens
		elif self.char in NUMBER_STARTCHARS:
			while self.char in NUMBER_CHARS:
				word = word + self.char
				self.char = self.scanner.getChar()
			token = Token(word)
			token.type = "NUMBER"

		# getting delimiters
		elif self.char in DELIMITER_SYMBOLS:
			token = Token(self.char)
			token.type = "DELIMITER"
			self.char = self.scanner.getChar()

		elif self.char in IDENTIFIER_STARTCHARS:
			while self.char in IDENTIFIER_CHARS:
				word = word + self.char
				self.char = self.scanner.getChar()
			token = Token(word)
			if word in RESERVED_WORDS:
				token.type = RESERVED
			else:
				token.type = "IDENTIFIER"

		else:
			self.char = self.scanner.getChar()
			token = Token("")
			token.type = "UNKNOWN"

		return token
