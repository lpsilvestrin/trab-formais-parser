import string

RESERVED_WORDS = ["if", "while", "def", "return"]
ONECHARSYMBOLS = ["+", "=", "-", ","]
COMPARATORS = [">", "<"]
OPERATORS = ["+", "-"]
DELIMITER_SYMBOLS = ["(", ")", "{", "}", ";"]

# characters that compose an indentifier
IDENTIFIER_STARTCHARS = string.letters
IDENTIFIER_CHARS = string.letters + string.digits

#characters that compose a number
NUMBER_STARTCHARS = string.digits + "-"
NUMBER_CHARS = string.digits

# wihte spaces

WHITESPACE_CHARS = [" ", "\t", "\n"]

# token types

IDENTIFIER = "IDENTIFIER"
NUMBER = "NUMBER"
WHITESPACE = "WHITESPACE"
DELIMITER = "DELIMITER"
RESERVED = "RESERVED"
COMPARATOR = "COMPARATOR"
