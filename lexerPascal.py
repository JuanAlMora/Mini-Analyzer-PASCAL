'''Analizador lexico de mini Pascal.
Integrantes:
-Sebastian Buitrago
-Juan Esteban Corrales
-Juan Alejandro Mora
'''
from ast import Pass
import ply.lex as lex
import ply.yacc as yacc
import sys

#lista de tokens
tokens = (
    #palabras reservadas
    'ARRAY',
    'BEGIN',
    'CONST',
    'CHAR',
    'DOWNTO',
    'END',
    'FOR',
    'FUNCTION',
    'IF',
    'INPUT',
    'OUTPUT',
    'LABEL',
    'NIL',
    'PROGRAM',
    'REPEAT',
    'TO',
    'WITH',
    'CASE',
    'DO',
    'ELSE',
    'FILE',
    'GOTO',
    'OF',
    'PACKED',
    'PROCEDURE',
    'RECORD',
    'SET',
    'THEN',
    'TYPE',
    'UNTIL',
    'VAR',
    'WHILE',
    'FALSE',
    'TRUE',
    'SIN',
    'COS',
    'SQRT',
    'SQR',
    'EXP',
    'LN',
    'DIV',
    'MOD',
    'INTEGER',
    'BOOLEAN',
    'WRITE',
    'READ',
    'USES',
    'REAL',
    #simbolos
    'PLUS',             #+
    'MINUS',            #-
    'TIMES',             #*
    'DIVIDE',           #/
    'LESS',             #<
    'LESSEQUAL',        #<=
    'GREATER',          # >
    'GREATEREQUAL',     # >=
    'EQUAL',            # =
    'DEQUAL',           #<>
    'COMMA',            #,
    'LPAREN',           #(
    'RPAREN',           #)
    'LBRACKET',         #{
    'RBRACKET',         #}
    'LBLOCK',           #[
    'RBLOCK',           #]
    'COLON',            #:
    'AMPERSANT',        #&
    'HASHTAG',          ##
    'DOT',              #.
    'QUOT',             #' 
    'POT',              #^
    'DISTINT',          #!
    'SEMICOLON',        #;
    #Otros
    'NUMBER',
    'ID',
    'COMMENTBLOCK',
    'COMMENTLINE',
    'STRING'
)
#Reglas ER
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUAL  = r'='
t_DISTINT = r'!'
t_LESS   = r'<'
t_GREATER = r'>'
t_SEMICOLON = r';'
t_COMMA  = r','
t_LPAREN = r'\('
t_RPAREN  = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LBLOCK   = r'{'
t_RBLOCK   = r'}'
t_COLON   = r':'
t_AMPERSANT = r'\&'
t_HASHTAG = r'\#'
t_DOT = r'\.'
t_QUOT = r'\''

#Funciones Palabras Reservadas
def t_ARRAY(t):
    r'array'
    return t

def t_BEGIN(t):
    r'begin'
    return t

def t_CONST(t):
    r'const'
    return t

def t_DOWNTO(t):
    r'downto'
    return t

def t_END(t):
    r'end'
    return t

def t_FOR(t):
    r'for'
    return t

def t_FUNCTION(t):
    r'function'
    return t

def t_WRITE(t):
    r'write'
    return t

def t_READ(t):
    r'read'
    return t

def t_CHAR(t):
    r'char'
    return t

def t_USES(t):
    r'uses'
    return t
def t_INPUT(t):
    r'input'
    return t

def t_OUTPUT(t):
    r'output'
    return t

def t_IF(t):
    r'if'
    return t

def t_NIL(t):
    r'nil'
    return t
   
def t_PROGRAM(t):
    r'program'
    return t  

def t_REPEAT(t):
    r'repeat'
    return t

def t_TO(t):
    r'to'
    return t

def t_WITH(t):
    r'with'
    return t
    
def t_CASE(t):
    r'case'
    return t  

def t_DO(t):
    r'do'
    return t          
   
def t_ELSE(t):
    r'else'
    return t

def t_FILE(t):
    r'file'
    return t
    
def t_GOTO(t):
    r'goto'
    return t   

def t_PACKED(t):
    r'packed'
    return t

def t_OF(t):
    r'of'
    return t
    
def t_PROCEDURE(t):
    r'procedure'
    return t

def t_RECORD(t):
    r'record'
    return t    

def t_SET(t):
    r'set'
    return t

def t_THEN(t):
    r'THEN'
    return t 

def t_TYPE(t):
    r'type'
    return t 

def t_REAL(t):
    r'real'
    return t 
     
def t_UNTIL(t):
    r'until'
    return t 

def t_VAR(t):
    r'var'
    return t

def t_WHILE(t):
    r'while'
    return t

def t_FALSE(t):
    r'false'
    return t

def t_TRUE(t):
    r'true'
    return t
    
def t_SIN(t):
    r'sin'
    return t

def t_COS(t):
    r'cos'
    return t

def t_SQRT(t):
    r'sqrt'
    return t

def t_EXP(t):
    r'exp'
    return t

def t_LN(t):
    r'ln'
    return t

def t_DIV(t):
    r'div'
    return t

def t_MOD(t):
    r'mod'
    return t

def t_INTEGER(t):
    r'integer'
    return t

def t_BOOLEAN(t):
    r'boolean'
    return t

def t_GREATEQUAL(t):
    r'>='
    return t

def t_LESSEQUAL(t):
    r'<='
    return t

def t_DEQUAL(t):
    r'<>'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

#Otros
def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t

def t_ID(t):
    r'\w+(_\d\w)*'
    return t

def t_STRING(t):               #omitir las cadenas
    r'\'([^\\\n]|(\\.))*?\''
    return t

t_ignore = ' \t' 

 
def t_COMMENTBLOCK(t):
    r'{(.|\n)*?\}'
    t.lexer.lineno += t.value.count('\n')

def t_COMMENTLINE(t):
    r'//(.)*?\n'
    t.lexer.lineno += 1

#-------------------------------------------

def t_error(t):
    print ("Lexical error: " + str(t.value[0]))
    t.lexer.skip(1)

def test(data, lexer):                        #realiza el analisis de los tokens
	lexer.input(data)
	while True:
		tok = lexer.token()    #recolecta los tokens segun las reglas que tenemos
		if not tok:
			break
		print (tok)       #imprime la informacion del token encontrado

lexer = lex.lex()                #construir el lexer

if __name__ == '__main__':
	if (len(sys.argv) > 1):
		fin = sys.argv[1]
	else:
		fin = 'prueba.pas'              #leer el archivo txt
	f = open(fin, 'r')
	data = f.read()
	print (data)
	lexer.input(data)
	test(data, lexer)