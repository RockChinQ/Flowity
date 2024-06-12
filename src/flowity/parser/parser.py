import ply.yacc as yacc

# Get the token map from the lexer. This is required.
from .lex import tokens, lexer

# Grammar rules and actions
def p_program(p):
    '''program : statement_list'''
    p[0] = ('program', p[1])

def p_statement_list(p):
    '''statement_list : statement
                      | statement statement_list'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[2]

def p_statement(p):
    '''statement : prompt
                 | assignment
                 | function_call'''
    p[0] = p[1]

def p_prompt(p):
    '''prompt : PROMPT'''
    p[0] = ('prompt', p[1])

def p_assignment(p):
    '''assignment : VARIABLE EQUALS expression'''
    p[0] = ('assignment', p[1], p[3])

def p_function_call(p):
    '''function_call : VARIABLE LPAREN argument_list RPAREN'''
    p[0] = ('function_call', p[1], p[3])

def p_argument_list(p):
    '''argument_list : expression
                     | expression COMMA argument_list
                     | empty'''
    if len(p) == 2:
        p[0] = [p[1]]
    elif len(p) == 4:
        p[0] = [p[1]] + p[3]
    else:
        p[0] = []

def p_expression(p):
    '''expression : VARIABLE
                  | STRING
                  | function_call'''
    p[0] = p[1]

def p_empty(p):
    '''empty :'''
    p[0] = None

# Error rule for syntax errors
def p_error(p):
    print(f"Syntax error at '{p.value}'")

# Build the parser
parser = yacc.yacc()

# Example input
# input_code = '''
# Hello, who are you?

# $str = $query()

# 你好，我叫Rock！

# $str0 = $query()
# $end($str)
# '''

# # Tokenize and parse the input code
# lexer.input(input_code)
# for tok in lexer:
#     print(tok)

# result = parser.parse(input_code)
# print(result)
