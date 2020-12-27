import re

def isOperator(a):
    for o in operators:
        if o == a:
            return True

def isInteger(a):
    
    if integer_pattern.fullmatch(a) is not None:
        return True

def isFloat(a):
    if float_pattern.fullmatch(a) is not None:
        return True

def isKeyWord(a):
    for key in keywords:
        if key == a:
            return True

def isLogicalOperator(a):
    for o in logical_operators:
        if a == o:
            return True

def isString(buf):
    if string_pattern.fullmatch(buf) is not None:
        return True

def isIdentifier(buf):
    if identifier_pattern.fullmatch(buf) is not None:
        return True
                    
def isSeparator(a):
    
    if separator_pattern.fullmatch(a) is not None:
        return True

def isTerminal(a):
    
    if a == '$':
        return True

def isSpace(a):
    if a == ' ':
        return True

def isComment(a):
    if comment_pattern.fullmatch(a) is not None:
        return True

integer=0
string=0
float1=0
identifier=0
separator=0
oprator=0
logical_operator=0
keyword=0
terminal=0
comment=0

identifier_pattern=re.compile("[A-Za-z_][A-Za-z0-9_]*")
integer_pattern=re.compile(r"(\+|-)?[0-9]+")
separator_pattern=re.compile("[(){}|,; ]")
float_pattern=re.compile('[0-9]*.[0-9]+')
string_pattern=re.compile(r'(\"([^#\"]|\\.)*\")|(\'([^#\']|\\.)*\')')
comment_pattern=re.compile(r'\#.*\n')

f = open("Zorbaa.za", "r")
operators=['+','-','/','*','=','!','|','%']
logical_operators=["<=",">=","!=","==","<",">"]
keywords=["int","char","float","double","void","bool","for","while","do","if","else","print","input","return","fun","true","false"]

while True:
    a=f.readline()
    b=f.readline()
    if not a:
        break
    length=len(a)
    i=0
    buf=""
    while True:
        if not a:
            break

        if isSeparator(a[i]) == True or isTerminal(a[i]) == True or isOperator(a[i])==True or isLogicalOperator(buf)==True or isInteger(a[i])==True or isFloat(buf)==True or isString(buf)==True:
        
            if isKeyWord(buf) == True:
                keyword=keyword+1
                print('{} is Keyword'.format(buf))
                buf=''
                

            if isOperator(buf)==True:
                j=i
                logic=buf+a[i]
                
                if isLogicalOperator(logic) == True:
                    logical_operator=logical_operator+1
                    print('{} is Logical Operator'.format(logic))
                    i=i+1
                    buf=''
                elif (buf == "+" or buf == "-") and isInteger(a[i]) == True:
                    while True:
                        
                        if isSeparator(a[j+1]) == True or isTerminal(a[j+1])==True:
                            i=j
                            break
                        j=j+1
                        logic+=a[j]
                    
                    if isInteger(logic) == True:
                        integer=integer+1
                        print('{} is Integer'.format(logic))
                        i=i+1
                        buf=''
                        

                else:
                    #print(u)
                    oprator=oprator+1
                    print('{} is Operator'.format(buf))
                    buf=''
                        
            if isLogicalOperator(buf) == True:
                logic=buf+a[i]
                
                if isLogicalOperator(logic) == True:
                    logical_operator=logical_operator+1
                    print('{} is Logical Operator'.format(logic))
                    i=i+1
                    buf=''
                else:
                    logical_operator=logical_operator+1
                    print('{} is Logical Operator'.format(buf))
                    buf=''        
            
            if isFloat(buf) == True:
                float1=float1+1
                print('{} is Float'.format(buf))
                buf=''
            
            if isInteger(buf) == True:
                integer=integer+1
                print('{} is Integer'.format(buf))
                buf=''

            if isString(buf) == True:
                string=string+1
                print('{} is String'.format(buf))
                buf=''

            if isIdentifier(buf) == True:
                identifier=identifier+1
                print('{} is Identifier'.format(buf))
                buf=''

            if isTerminal(a[i])==True:
                terminal=terminal+1
                print('Terminal')
                
                buf=''

            #buf=''
               
        if a[i] != ' ':
            buf+=a[i]
            if separator_pattern.fullmatch(buf) is not None:
                separator=separator+1
                print('{} is Separator'.format(buf))
                buf=''

        i+=1
        if i >= length:
            if isComment(buf):
                comment=comment+1
                print("Comment")
            break
    
    if not b:
        break
    length=len(b)
    i=0
    buf=""
    while True:
        if not b:
            break
        
        if isSeparator(b[i]) == True or isTerminal(b[i]) == True or isOperator(b[i])==True or isInteger(b[i])==True or isFloat(buf)==True or isString(buf)==True:
            
            if isKeyWord(buf) == True:
                keyword=keyword+1
                print('{} is Keyword'.format(buf))
                buf=''
                

            if isOperator(buf)==True:
                j=i
                logic=buf+b[i]
                
                if isLogicalOperator(logic) == True:
                    logical_operator=logical_operator+1
                    print('{} is Logical Operator'.format(logic))
                    i=i+1
                    buf=''
                elif (buf == "+" or buf == "-") and isInteger(b[i]) == True:
                    while True:
                        
                        if isSeparator(b[j+1]) == True or isTerminal(b[j+1])==True:
                            i=j
                            break
                        j=j+1
                        logic+=b[j]
                    
                    if isInteger(logic) == True:
                        integer=integer+1
                        print('{} is Integer'.format(logic))
                        i=i+1
                        buf=''
                        

                else:
                    #print(u)
                    oprator=oprator+1
                    print('{} is Operator'.format(buf))
                    buf=''            

            if isLogicalOperator(buf)==True:
                logical_operator=logical_operator+1
                print('{} is Logical Operator'.format(buf))
                buf=''
                    
            
            if isFloat(buf) == True:
                float1=float1+1
                print('{} is Float'.format(buf))
                buf=''
            
            if isInteger(buf) == True:
                integer=integer+1
                print('{} is Integer'.format(buf))
                buf=''

            if isString(buf) == True:
                string=string+1
                print('{} is String'.format(buf))
                buf=''

            if isIdentifier(buf) == True:
                identifier=identifier+1
                print('{} is Identifier'.format(buf))
                buf=''

            if isTerminal(b[i])==True:
                terminal=terminal+1
                print('Terminal')
                buf=''

            #buf=''
               
        if b[i] != ' ':
            buf+=b[i]
            if separator_pattern.fullmatch(buf) is not None:
                separator=separator+1
                print('{} is Separator'.format(buf))
                buf=''

        i+=1
        if i >= length:
            if isComment(buf):
                comment=comment+1
                print("Comment")
            break
    
f.close()

print("\nNumber of Operators = {}, Number of Keywords = {}, Number of Identifiers = {}, Number of Logical Operators = {}, Number of Integers  = {}, Number of Floats = {}, Number of Strings = {}, Number of Separators = {}, Number of Terminals = {}, Number of Comments = {}\n".format(oprator, keyword, identifier, logical_operator, integer, float1, string, separator, terminal, comment))