import ply.yacc as yacc
from lexerPascal import tokens
import lexerPascal
import sys
import ply.yacc

VERBOSE = 1

def p_program(p):
	'program : PROGRAM  ID program_heading SEMICOLON block DOT'
	pass

def p_program_heading(p):
	'program_heading : LPAREN identifier_list RPAREN'
	pass
def p_identifier_list(p):
    '''identifier_list : ID
                       | identifier_list COMMA ID'''
def p_block(p):
	'''block : block1 
             | label_declaration SEMICOLON block1'''
	pass

def p_block1(p):
	'''block1 : block2 
              | constant_declaration SEMICOLON block2'''
	pass

def p_block2(p):
	'''block2 : block3 
              | type_declaration SEMICOLON block3'''
	pass

def p_block3(p):
	'''block3 : block4 
              | variable_declaration SEMICOLON block4'''
	pass

def p_block4(p):
	'''block4 : block5 
              | proc_and_func_declaration SEMICOLON block5'''
	pass

def p_block5(p):
	'block5 : BEGIN statement_list statement'            
	pass

def p_label_declaration(p):
    '''label_declaration : LABEL NUMBER
                         | label_declaration COMMA NUMBER'''
    pass

def p_constant_declaration(p):
    '''constant_declaration : CONST ID EQUAL constant
                            | constant_declaration SEMICOLON ID EQUAL constant'''
    pass

def p_type_declaration(p):
    '''type_declaration : type ID EQUAL type
                        | type_declaration SEMICOLON ID EQUAL type'''
    pass      

def p_variable_declaration(p):
    ''' variable_declaration : VAR variableid_list COLON type
                             | variable_declaration SEMICOLON variableid_list COLON type'''
    pass

def p_variableid_list(p):
    '''variableid_list : ID
                     | variableid_list COMMA ID'''
    pass    

def p_constant(p):
    '''constant : INTEGER
                | REAL
                | CHAR
                | BOOLEAN'''

def p_type(p):
    '''type : simple_type
            | structured_type
            | typeid '''
    pass   
       
def p_simple_type(p):
    '''simple_type : LPAREN indentifier_list RPAREN
                   | constant DOT DOT DOT constant
                   | typeid ''' 
    pass  
           
def p_structured_type(p):
    '''structured_type : ARRAY LBLOCK index_list RBLOCK OF type
                       | RECORD field_list END
                       | SET OF simple_type
                       | FILE OF type
                       | PACKED structured_type'''
    pass

def p_index_list(p):
    '''index_list : simple_type
                  | index_list COMMA simple_type'''
    pass

def p_field_list(p):
    '''index_list : fixed_part
                  | fixed_part SEMICOLON variant_part
                  | variant_part'''
    pass

def p_fixed_part(p):
    '''fixed_part : record_field
                  | fixed_part SEMICOLON record_field'''
    pass

def p_record_field(p):
    '''record_field : empty
                    | field_list COLON type'''
    pass

def p_fieldid_list(p):
    '''fieldid_list : ID
                    | fieldid_list COMMA ID'''
    pass


def p_variant_part(p):
	'''variant_part : CASE tag_field OF variant_list'''
	pass

def p_tag_field(p):
	'''tag_field : typeid 
				 | identifier COLON typeid'''
	pass

def p_variant_list(p):
	'''variant_list : variant 
					| variant_list SEMICOLON variant'''
	pass

def p_variant(p):
	'''variant : empty 
			   | case_label_list COLON LPAREN field_list RPAREN'''
	pass
 
def p_caseLabel_list(p):
	'''case_label_list : constant 
					   | case_label_list COMMA constant'''
	pass

def p_procAndFunc_declaration(p):
	'''proc_and_func_declaration : proc_or_func 
								 | proc_and_func_declaration SEMICOLON proc_or_func '''
	pass

def p_proc_or_func(p):
	'''proc_or_func : procedure identifier parametersopt SEMICOLON block_or_forward
		 			| function  identifier parametersopt COLON typeid SEMICOLON block_or_forward '''
	pass

def p_block_or_fordward(p):
	'''block_or_forward : block 
						| forward'''
	pass

def p_parameters(p):
	'''parameters : LPAREN formal_parameter_list RPAREN'''
	pass

def p_formal_parameter_list(p):
	'''formal_parameter_list : formal_parameter_section
		 	 				 | formal_parameter_list SEMICOLON formal_parameter_section'''
	pass

def p_formal_parameter_section(p):
	'''formal_parameter_section : parameterid_list COLON typeid 
							    | var parameterid_list COLON typeid 
								| procedure identifier parametersopt 
								| function identifier parametersopt COLON typeid'''	
	pass

def p_parameterid_list(p):
	'''parameterid_list : identifier 
					    | parameterid_list COMMA identifier'''
	pass

def p_statement_list(p):
	'''statement_list : statement 
					  | statement_list SEMICOLON statement'''
	pass

def p_statement(p): 
   '''statement : empty 
   				| variable EQUAL expression 
   				| begin statement_list END  
   				| IF expression THEN statement 
   				| IF expression THEN statement else statement  
   				| case expression OF case_list END  
   				| while expression DO statement  
  				| repeat statement_list until expression  
   				| for varid EQUAL for_list DO statement  
   				| procid  
   				| procid LPAREN expression_list RPAREN  
   				| goto label 
   				| with record_variable_list DO statement  
   				| label COLON statement'''	
   pass

def p_variable(p):
   '''variable  : identifier  
			    | variable LBRACKET subscript_list RBRACKET  
			    | variable COMMA fieldid  
			    | variable '''
   pass

def p_subscriptlist(p):
	'''subscript_list : expression  
    				  |	subscript_list COMMA expression'''
	pass

def p_caselist(p):  
   '''case_list : case_label_list COLON statement  
   				| case_list SEMICOLON case_label_list COLON statement'''
   pass

def p_forlist(p): 
	'''for_list : expression to expression  
    			| expression downto expression'''
	pass

def p_expression_list(p):
	'''expression_list : expression  
    				   | expression_list COMMA expression'''
	pass
	
def p_label(P):  
   '''label : unsigned_integer'''
   pass

def p_record_variable_list(p):
	'''record_variable_list : variable  
    						| record_variable_list COMMA variable''' 
	pass


def p_expression(p):
   '''expression : expression relational_op additive_expression 
   				 | additive_expression''' 
   pass

def p_relationalop(p):
   '''relational_op : one OF 
   					| LESS  LESSEQUAL  EQUAL  DEQUAL  GREATEREQUAL  GREATER''' #  <> Como hacer eso 
   pass
	
def p_additive_expression(P): 
   '''additive_expression : additive_expression additive_op multiplicative_expression 
   						  | multiplicative_expression''' 
   pass

def p_additiveop(p): 
   '''additive_op : one OF 
   				  |	PLUS  MINUS  OR'''
   pass

def p_multiplicative_expression(p): 
   '''multiplicative_expression : multiplicative_expression multiplicative_op unary_expression 
   								| unary_expression'''
   pass
   
def p_multiplicative_op(p): 
   '''multiplicative_op : one OF  
   					    | TIMES  DIVIDE  div  MOD  AND  IN'''
   pass

def p_unary_expression(P): 
   '''unary_expression : unary_op unary_expression 
   					   | primary_expression'''  
   pass

def p_unaryop(p):  
	'''unary_op : one OF 
				| PLUS MINUS not'''	
	pass

def p_primary_expression(p):  
   '''primary_expression : variable 
						 | unsigned_integer 
						 | unsigned_real 
						 | string 
						 | nil 
						 | funcid LPAREN expression_list RPAREN 
						 | LBRACKET element_list RBRACKET 
						 | LPAREN expression RPAREN'''
   pass

def p_elementlist(p):  
   '''element_list : empty 
				   | element 
				   | element_list COMMA element'''
   pass

def p_element(p):  
   '''element : expression 
   			  | expression DOT DOT DOT expression'''
   pass

def p_constid(p):  
   '''constid : identifier'''
   pass

def p_typeid(p):
	'''typeid : identifier'''
	pass

def p_funcid(p):
	'''funcid : identifier'''
	pass 

def p_procid(p):
	'''procid : identifier'''
	pass

def p_fieldid(p):
	'''fieldid : identifier''' 
	pass

def p_varid(p):
	'''varid : identifier'''
	pass


def empty(p):
	''''''
	pass

def p_error(p):
	if VERBOSE:
		if p is not None:
			print ("ERROR SINTACTICO EN LA LINEA " + str(p.lexer.lineno) + " NO SE ESPERABA EL Token  " + str(p.value))
		else:
			print ("ERROR SINTACTICO EN LA LINEA: " + str(lexerPascal.lexer.lineno))
	else:
		raise Exception('syntax', 'error')
		

parser = yacc.yacc()

if __name__ == '__main__':

	if (len(sys.argv) > 1):
		fin = sys.argv[1]
	else:
		fin = 'prueba.txt'

	f = open(fin, 'r')
	data = f.read()
	#print (data)
	parser.parse(data, tracking=True)
	print("Amiguito, tengo el placer de informa que Tu parser reconocio correctamente todo")
	#input() 


                                     