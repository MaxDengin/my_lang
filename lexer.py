from rply import LexerGenerator
from globs import *

lg = LexerGenerator()
lg.add('FLOAT', '-?\d+\.\d+')
lg.add('INTEGER', '-?\d+')
lg.add('NULL', 'null(?!\w)')
lg.add('STRING', '(""".*?""")|(".*?")|(\'.*?\')')
lg.add('PRINT', 'print(?!\w)')
lg.add('BOOLEAN', f"{TRUE}(?!\w)|{FALSE}(?!\w)")
lg.add('IF', 'if(?!\w)')
lg.add('ELSE', 'else(?!\w)')
lg.add('AND', "and(?!\w)")
lg.add('OR', "or(?!\w)")
lg.add('NOT', "not(?!\w)")
lg.add('WHILE', 'while(?!\w)')
lg.add('END', 'end(?!\w)')
lg.add('IDENTIFIER', "[a-zA-Z_][a-zA-Z0-9_]*")
lg.add('PLUS', '\+')
lg.add('==', '==')
lg.add('COLON', ':')
lg.add('!=', '!=')
lg.add('>=', '>=')
lg.add('<=', '<=')
lg.add('>', '>')
lg.add('<', '<')
lg.add('=', '=')
lg.add('[', '\[')
lg.add(']', '\]')
lg.add('{', '\{')
lg.add('}', '\}')
lg.add(',', ',')
lg.add('DOT', '\.')
lg.add('MINUS', '-')
lg.add('MUL', '\*')
lg.add('DIV', '/')
lg.add('MOD', '%')
lg.add('(', '\(')
lg.add(')', '\)')
lg.add('NEWLINE', '\n')

lg.ignore(r'[ \t\r\f\v]+')
lg.ignore(r'#.*\n')

lexer = lg.build()




# with open('test.txt', 'r', encoding='utf-8') as f:
#     text = f.read()

# tokens = lexer.lex(text)

# for token in tokens:
#     print(token)