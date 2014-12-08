#!/usr/bin/python

import sys
from scanner import Scanner
from lexical_rules import *
from lexer import Lexer
from token import Token
from parser import Parser

filename = str(sys.argv[1])

lexer = Lexer(filename)
tokenList = []
tok = lexer.getToken()
while tok.type != "EOF":
	tokenList.append(tok)
	print tok.type + " > " + tok.text
	tok = lexer.getToken()
tokenList.append(tok)
parser = Parser(tokenList)
print parser.parse()