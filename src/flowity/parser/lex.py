# The first lex that only supports basic querying.

import ply.lex as lex

# List of token names
tokens = (
    'STRING', 'VARIABLE', 'EQUALS', 'LPAREN', 'RPAREN', 'COMMA', 'PROMPT'
)

# Regular expression rules for simple tokens
t_EQUALS = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','

# Define a rule for variables (identifiers starting with $)
def t_VARIABLE(t):
    r'\$[a-zA-Z_][a-zA-Z_0-9]*'
    return t

# Define a rule for strings (enclosed in double quotes)
def t_STRING(t):
    r'\"([^\\\n]|(\\.))*?\"'
    return t

# Define a rule for prompts (any text not captured by other rules)
def t_PROMPT(t):
    r'[^\$=()\n]+'
    t.value = t.value.strip()
    return t

# Define a rule for ignoring comments and whitespace
t_ignore_COMMENT = r'//.*'
t_ignore = ' \t\n'

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
