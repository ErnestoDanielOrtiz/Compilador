#Importar lex & yacc de ply

from ply import lex
import ply.yacc as yacc
import sys
import re

errorSem = False #No se imprime aceptado en caso de algún error

#Inicio Lexer

#Palabras reservadas
reserved = {'program' :"PROGRAM",
    'function':"FUNCION",
    'if':"IF",
    'else':"ELSE",
    'while':"WHILE",
    'do':"DO",
    'for':"FOR",
    'int':"INT",
    'float':"FLOAT",
    'char':"CHAR",
    'bool':"BOOL",
    'void':"VOID",
    'null':"NULL",
    'TRUE':"CTE_BOOL",
    'FALSE':"CTE_BOOL",
    'main':"MAIN",
    'read':"READ",
    'print':"PRINT",
    'return' : "RETURN",

}

#Tokens
tokens=[
"CTE_INT",
"CTE_FLOAT",
"CTE_CHAR",
"CTE_STRING",
"ID",
"COLON",
"SEMICOLON",
"COMMA",
"EQ",
"EXLAM",
"OPENPAR",
"CLOSEPAR",
"GT",
"LT",
"PLUS",
"MINUS",
"MUL",
"DIV",
"OPENCUR",
"CLOSECUR",
"OPENSQU",
"CLOSESQU",
"AND",
"OR",
"DLR"] + list(reserved.values())


#Ints
def t_CTE_INT(t):
    r"[0-9]+"
    t.value = int(t.value)
    return t

#Floats
def t_CTE_FLOAT(t):
    r"[0-9]+\.[0-9]+([eE][+-]?[0-9]+)?"
    t.value = float(t.value)
    return t

#Chars
t_CTE_CHAR = ("\'[^\']\'")

#ID
def t_ID(t): 
    r"[a-zA-Z]([a-zA-Z]|[0-9]|[_])*"
    t.type = reserved.get(t.value,'ID')
    return t

t_COLON = (":")
t_SEMICOLON = (";")
t_COMMA = (",")
t_EQ = ("=")
t_OPENPAR = ("\(")
t_CLOSEPAR = ("\)")
t_GT = ("<")
t_LT = (">")
t_PLUS = ("\+")
t_MINUS = ("\-")
t_MUL = ("\*")
t_DIV = ("/")
t_OPENCUR = ("{")
t_CLOSECUR = ("}")
t_OPENSQU = (r"\[")
t_CLOSESQU = (r"\]")
t_AND = (r"\&\&")
t_OR = (r"\|\|")
t_EXLAM = (r"!")
t_DLR = (r"\$")
t_ignore  = ' \t'

def t_newline(t):
    r'\n'
    t.lexer.lineno += len(t.value) 

def t_error(t):
     print("Token Invalido '%s' en la linea %r" % (t.value[0],t.lexer.lineno) )

lexer = lex.lex()
#Fin del lexer

#Inicio Cubo Semántico
cuboSem = {
           '=':{'int':{
                          'int':'int',
                          'float': 'int',
                          'char':'int',
                          'bool': 'char',
                          'string':'error'
                        },
                'float':{
                          'int':'float',
                          'float': 'float',
                          'char':'float',
                          'bool': 'float',
                          'string':'error'
                        },
                'char':{
                          'int':'char',
                          'float': 'char',
                          'char':'char',
                          'bool': 'char',
                          'string':'error'
                        },
                'bool':{
                          'int':'bool',
                          'float': 'bool',
                          'char':'bool',
                          'bool': 'bool',
                          'string':'error'
                        },
                'string':{
                          'int':'error',
                          'float': 'error',
                          'char':'error',
                          'bool': 'error',
                          'string':'string'
                        },

                },
           '||':{
               'int':{
                          'int':'bool',
                          'float': 'bool',
                          'char':'bool',
                          'bool': 'bool',
                          'string':'error'
                        },
                'float':{
                          'int':'bool',
                          'float': 'bool',
                          'char':'bool',
                          'bool': 'bool',
                          'string':'error'
                        },
                'char':{
                          'int':'bool',
                          'float': 'bool',
                          'char':'bool',
                          'bool': 'bool',
                          'string':'error'
                        },
                'bool':{
                          'int':'bool',
                          'float': 'bool',
                          'char':'bool',
                          'bool': 'bool',
                          'string':'error'
                        },
                'string':{
                          'int':'error',
                          'float': 'error',
                          'char':'error',
                          'bool': 'error',
                          'string':'bool'
                        },},
           '&&':{
                'int':{
                          'int':'bool',
                          'float': 'bool',
                          'char':'bool',
                          'bool': 'bool',
                          'string':'error'
                        },
                'float':{
                          'int':'bool',
                          'float': 'bool',
                          'char':'bool',
                          'bool': 'bool',
                          'string':'error'
                        },
                'char':{
                          'int':'bool',
                          'float': 'bool',
                          'char':'bool',
                          'bool': 'bool',
                          'string':'error'
                        },
                'bool':{
                          'int':'bool',
                          'float': 'bool',
                          'char':'bool',
                          'bool': 'bool',
                          'string':'error'
                        },
                'string':{
                          'int':'error',
                          'float': 'error',
                          'char':'error',
                          'bool': 'error',
                          'string':'bool'
                        },
           },
            '>':{
                'int':{
                          'int':'bool',
                          'float': 'bool',
                          'char':'bool',
                          'bool': 'bool',
                          'string':'error'
                        },
                'float':{
                          'int':'bool',
                          'float': 'bool',
                          'char':'bool',
                          'bool': 'bool',
                          'string':'error'
                        },
                'char':{
                          'int':'bool',
                          'float': 'bool',
                          'char':'bool',
                          'bool': 'bool',
                          'string':'error'
                        },
                'bool':{
                          'int':'bool',
                          'float': 'bool',
                          'char':'bool',
                          'bool': 'bool',
                          'string':'error'
                        },
                'string':{
                          'int':'error',
                          'float': 'error',
                          'char':'error',
                          'bool': 'error',
                          'string':'bool'
                        },
           },
           '<':{
                'int':{
                          'int':'bool',
                          'float': 'bool',
                          'char':'bool',
                          'bool': 'bool',
                          'string':'error'
                        },
                'float':{
                          'int':'bool',
                          'float': 'bool',
                          'char':'bool',
                          'bool': 'bool',
                          'string':'error'
                        },
                'char':{
                          'int':'bool',
                          'float': 'bool',
                          'char':'bool',
                          'bool': 'bool',
                          'string':'error'
                        },
                'bool':{
                          'int':'bool',
                          'float': 'bool',
                          'char':'bool',
                          'bool': 'bool',
                          'string':'error'
                        },
                'string':{
                          'int':'error',
                          'float': 'error',
                          'char':'error',
                          'bool': 'error',
                          'string':'bool'
                        },
           },
            '>=':{
                'int':{
                          'int':'bool',
                          'float': 'bool',
                          'char':'bool',
                          'bool': 'bool',
                          'string':'error'
                        },
                'float':{
                          'int':'bool',
                          'float': 'bool',
                          'char':'bool',
                          'bool': 'bool',
                          'string':'error'
                        },
                'char':{
                          'int':'bool',
                          'float': 'bool',
                          'char':'bool',
                          'bool': 'bool',
                          'string':'error'
                        },
                'bool':{
                          'int':'bool',
                          'float': 'bool',
                          'char':'bool',
                          'bool': 'bool',
                          'string':'error'
                        },
                'string':{
                          'int':'error',
                          'float': 'error',
                          'char':'error',
                          'bool': 'error',
                          'string':'bool'
                        },
           },
            '<=':{
                'int':{
                          'int':'bool',
                          'float': 'bool',
                          'char':'bool',
                          'bool': 'bool',
                          'string':'error'
                        },
                'float':{
                          'int':'bool',
                          'float': 'bool',
                          'char':'bool',
                          'bool': 'bool',
                          'string':'error'
                        },
                'char':{
                          'int':'bool',
                          'float': 'bool',
                          'char':'bool',
                          'bool': 'bool',
                          'string':'error'
                        },
                'bool':{
                          'int':'bool',
                          'float': 'bool',
                          'char':'bool',
                          'bool': 'bool',
                          'string':'error'
                        },
                'string':{
                          'int':'error',
                          'float': 'error',
                          'char':'error',
                          'bool': 'error',
                          'string':'bool'
                        },
           },
           '==':{
                'int':{
                          'int':'bool',
                          'float': 'bool',
                          'char':'bool',
                          'bool': 'bool',
                          'string':'error'
                        },
                'float':{
                          'int':'bool',
                          'float': 'bool',
                          'char':'bool',
                          'bool': 'bool',
                          'string':'error'
                        },
                'char':{
                          'int':'bool',
                          'float': 'bool',
                          'char':'bool',
                          'bool': 'bool',
                          'string':'error'
                        },
                'bool':{
                          'int':'bool',
                          'float': 'bool',
                          'char':'bool',
                          'bool': 'bool',
                          'string':'error'
                        },
                'string':{
                          'int':'error',
                          'float': 'error',
                          'char':'error',
                          'bool': 'error',
                          'string':'bool'
                        },
           },
           '!=':{
                'int':{
                          'int':'bool',
                          'float': 'bool',
                          'char':'bool',
                          'bool': 'bool',
                          'string':'error'
                        },
                'float':{
                          'int':'bool',
                          'float': 'bool',
                          'char':'bool',
                          'bool': 'bool',
                          'string':'error'
                        },
                'char':{
                          'int':'bool',
                          'float': 'bool',
                          'char':'bool',
                          'bool': 'bool',
                          'string':'error'
                        },
                'bool':{
                          'int':'bool',
                          'float': 'bool',
                          'char':'bool',
                          'bool': 'bool',
                          'string':'error'
                        },
                'string':{
                          'int':'error',
                          'float': 'error',
                          'char':'error',
                          'bool': 'error',
                          'string':'bool'
                        },
           },
           '+':{
                'int':{
                          'int':'int',
                          'float': 'float',
                          'char':'int',
                          'bool': 'int',
                          'string':'error'
                        },
                'float':{
                          'int':'float',
                          'float': 'float',
                          'char':'float',
                          'bool': 'float',
                          'string':'error'
                        },
                'char':{
                          'int':'int',
                          'float': 'float',
                          'char':'int',
                          'bool': 'int',
                          'string':'error'
                        },
                'bool':{
                          'int':'int',
                          'float': 'float',
                          'char':'int',
                          'bool': 'int',
                          'string':'error'
                        },
                'string':{
                          'int':'error',
                          'float': 'error',
                          'char':'error',
                          'bool': 'error',
                          'string':'string'
                        },
                'none' : {
                    'int' : 'int',
                    'float' : 'float',
                    'char' : 'error',
                    'bool' : 'error',
                    'string' : 'error'
                }
           },
           '-':{
                'int':{
                          'int':'int',
                          'float': 'float',
                          'char':'int',
                          'bool': 'int',
                          'string':'error',
                        },
                'float':{
                          'int':'float',
                          'float': 'float',
                          'char':'float',
                          'bool': 'float',
                          'string':'error'
                        },
                'char':{
                          'int':'int',
                          'float': 'float',
                          'char':'int',
                          'bool': 'int',
                          'string':'error'
                        },
                'bool':{
                          'int':'int',
                          'float': 'float',
                          'char':'int',
                          'bool': 'int',
                          'string':'error'
                        },
                'string':{
                          'int':'error',
                          'float': 'error',
                          'char':'error',
                          'bool': 'error',
                          'string':'error'
                        },
                'none' : {
                    'int' : 'int',
                    'float' : 'float',
                    'char' : 'error',
                    'bool' : 'error',
                    'string' : 'error'
                }

           },
           '*':{
                'int':{
                          'int':'int',
                          'float': 'float',
                          'char':'int',
                          'bool': 'int',
                          'string':'error'
                        },
                'float':{
                          'int':'float',
                          'float': 'float',
                          'char':'float',
                          'bool': 'float',
                          'string':'error'
                        },
                'char':{
                          'int':'int',
                          'float': 'float',
                          'char':'int',
                          'bool': 'int',
                          'string':'error'
                        },
                'bool':{
                          'int':'int',
                          'float': 'float',
                          'char':'int',
                          'bool': 'int',
                          'string':'error'
                        },
                'string':{
                          'int':'error',
                          'float': 'error',
                          'char':'error',
                          'bool': 'error',
                          'string':'error'
                        },
           },
           '/':{
               'int': {
                   'int': 'int',
                   'float': 'float',
                   'char': 'int',
                   'bool': 'int',
                   'string': 'error'
               },
               'float': {
                   'int': 'float',
                   'float': 'float',
                   'char': 'float',
                   'bool': 'float',
                   'string': 'error'
               },
               'char': {
                   'int': 'int',
                   'float': 'float',
                   'char': 'int',
                   'bool': 'int',
                   'string': 'error'
               },
               'bool': {
                   'int': 'int',
                   'float': 'float',
                   'char': 'int',
                   'bool': 'int',
                   'string': 'error'
               },
               'string': {
                   'int': 'error',
                   'float': 'error',
                   'char': 'error',
                   'bool': 'error',
                   'string': 'error'
               },

           }
           }
#Fin Cubo Semántico

#Pilas
pOper = ['?']       #Pila de operadores
pilaOper = ['?']    #Pila de operandos
pTipo = ['?']       #Pila de tipos

#Precedencia
precedence = (
    ( 'left', 'PLUS', 'MINUS' ),
    ( 'left', 'MUL', 'DIV' ),
    ( 'nonassoc', 'GT', 'LT','AND','OR' ),
)