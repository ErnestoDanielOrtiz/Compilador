#Importar lex & yacc de ply

from ply import lex
import ply.yacc as yacc
import sys
import re

errorSem = False 

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
    t.vtype = reserved.get(t.value,'ID')
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

#Inicio Cubo Semantico
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
#Fin Cubo Semantico

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

#Funciones
dirFunc = {}

#Scope actual
currentScope = None

#Parametro evaluado
funcAllCurr = None

#Direcciones
nINTS = 1000
nFLOATS = 1000
nCHARS = 1000
nBOOLS = 1000
nPOINTERS = 1000

#Globales
globInt = 1000
globFloat = 2000
globChar = 3000
globBool = 4000

#Locales
locInt = 5000
locFloat = 6000
locChar = 7000
locBool = 8000

#Temporales
tempInt = 9000
tempFloat = 10000
tempChar = 11000
tempBool = 12000

#Constantes
constInt = 13000
constFloat = 14000
constChar = 15000
constBool = 16000

def virtualAdress(tableVar, adscope, nline):
  global globInt
  global globFloat
  global globChar
  global globBool

  global locInt
  global locFloat
  global locChar
  global locBool
  global tempInt

  global nINTS
  global nFLOATS
  global nCHARS
  global nBOOLS

  if (adscope == 'global'):
    for k in tableVar.keys():
      if ('dims' in tableVar[k].keys()):
        increase = tableVar[k]['size']
      else:
        increase = 1
      
      #if (tableVar[k]['vtype'] == 'int'):
        #if (nINTS < )

#Sintaxis
def p_PROGRAM(p):

  global dirFunc

  #Actualiza el directorio de funciones
  if(p[5] != None):
    dirFunc.update(p[5])
  
def p_PROG(p):
  print(test)
  
def p_GLOBVAR(p):
  global dirFunc
  
  #Numero de variables 
  nInt = 0
  nFloat = 0
  nChar = 0
  nBool = 0

  dirFunc['global'] = {'vtype': 'void', 'parameters': None, 'tableVar': p[1], 'variables': {'int': nInt, 'float': nFloat, 'char': nChar, 'bool': nBool}}

def p_STATEMENTS(p):
  if (p[1] == None):
    p[0] = None
  else:
    tableVar = {}
    tableVar.update(p[1])

    if(p[2] != None):
      checkexistance = p[1].keys()
      for k in checkexistance:
        if(k in p[2].keys()):
          print("Variables with 1 or more definitions")
        tableVar.update(p[2])

      p[0] = tableVar

def p_STATEMENT(p):
  p[0] = p[1]

def p_VAR(p):
  
  global currentScope
  global dirFunc

  #Numero de variables 
  nInt = 0
  nFloat = 0
  nChar = 0
  nBool = 0

  currentScope = 'main'

  #Global scope

  dirFunc['main'] = {'vtype': 'void', 'parameters': None, 'tableVar': p[1], 'variables': {'int': nInt, 'float': nFloat, 'char': nChar, 'bool': nBool}}

  p[0] = p[2]

def p_ARRDECL(p):
  sizeArr = 0
  array = {p[2]: {'vtype': p[1]}}
  array[p[2]].update(p[3])

def p_DIMONE(p):
  if(p[2] < 0):
    print("Invalid array length")

def p_DIMTWO(p):
  if(p[1] == None):
    p[0] = None
  else:
    if (p[2] < 0):
      print("Invalid array length")

def p_TYPE(p):
  p[0] = p[1]
  
def p_FUNCDIR(p):
  if(p[1] == None):
    p[0] = p[1]
  else:
    functions = {}
    functions.update(p[1])
    if(p[2] != None):
      for f in p[1].keys():
        if f in p[2].keys():
          print("Function has 1 or more definitions")
      functions.update(p[2])
    p[0] = functions

def p_FUNCDECL(p):
  p[0] = p[1]

def p_FUNCTION(p):
  global dirFunc
  global currentScope

  funcInput = {p[p3]: {'vtype': p[2], 'parameters': {}, 'start': p[1]}}
  currentScope = p[3]
  dirFunc.update({p[3]: {'vtype': p[2]}, 'parameters': {}})

  tableVarLocal = {}

  #Revisa si entran parametros y los agrega a la tabla de variables local
  if(p[5] != None):
    aux = {}
    aux.update(p[5])
    aux.update(tableVarLocal)
    tableVarLocal = aux
    funcInput[p[3]].update({'tableVar': tableVarLocal})
    funcInput[p[3]].update({'parameters': p[5]})
  
  dirFunc.update(funcInput)

  #Revisa que no se dupliquen los parametros no se declaren dentro de la funcion
  if(p[8] != None):
    for v in tableVar.keys():
      if(v in p[8].keys()):
        print("Variable already defined")
    tableVarLocal.update(p[8])

  funcInput[p[3]].update({'tableVar' : tableVarLocal})
  dirFunc.update(funcInput)
  p[0] = funcInput

def p_FUNCPAR(p):
    p[0] = p[1]

def p_PAR(p):
    funcPar = {p[2]: {'vtype': p[1]}}

    #Revisa si el parametro es un arreglo
    if(p[3] != None): 
      funcPar[p[2]].update(p[3])

    if(p[4] != None):
      if(p[2] in p[4].keys()):
        print("Variable already defined")
      else:
        funcPar.update(p[4])
    p[0] = funcPar

def p_PARAMETERS(p):
    if(p[1] != None):
      p[0] = p[2]
    else:
      p[0] = p[1]

def p_FUNCTYPE(p):
    p[0] = p[1]

def p_RETURN(p):
  print('test')

def p_BLOCK(p):
    print('test')

def p_ASSIGNATION(p):
  global cuboSem
  global dirFunc

  varType = None
  if p[2] == "-":
    if(p[1] in dirFunc[currentScope]['tableVar'].keys()):
      varType = dirFunc[currentScope]['tableVar'][p[1]]['vtype']
    elif(p[1] in dirFunc['global']['tableVar'].keys()):
      varType = dirFunc['global']['tableVar'][p[1]]['vtype']
    else:
      print("Variable not defined")
    
    assign = pilaOper.pop()
    assignType = pTipo.pop()

    if (cuboSem['='][varType][assignType] != 'error'):
      #print (cuboSem['='][varType][assignType])
      pass
    else:
      print("Assignment error")
  else:
    pass 

def p_CONDITION(p):
  print('test')

def p_ELSE(p):
  print('test')

def p_LOOP(p):
  print('test')

def p_WHILE(p):
  print('test')

def p_FOR(p):
  print('test')

