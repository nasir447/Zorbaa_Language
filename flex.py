#flex using python for Zorbaa Language
#
#Name: Nasir Khalil
#Roll Number: cs181005
#date: 28*12*2020





#import re

def isOperator(a):
    for o in operators:
        if o == a:
            return True
    return False

def isInteger(a):
    intiger_bool=False
    if len(a)!=0:
        
        if ord(a[0])==45:
            x=1;
            length1=len(a)
            
            while x<length1:
                if ord(a[x])>=48 and ord(a[x])<=57:
                    intiger_bool=True
                else:
                    intiger_bool=False
                    break
                x=x+1
        else:
            x=0;
            length1=len(a)
            while x<length1:
                if ord(a[x])>=48 and ord(a[x])<=57:
                    intiger_bool=True
                else:
                    intiger_bool=False
                    break
                x=x+1
    
    return intiger_bool


def isKeyWord(a):
    iskey =False
    x=0
    for key in keywords:
        if len(key) == len(a):
            o=x
            length1=len(key)
            while length1>o:
                if key[o] != a[o]:
                    iskey=False
                    x=o
                    break
                elif key[o] == a[o]:
                    iskey=True
                o=o+1
            if iskey == True:
                break
    return iskey

def isLogicalOperator(a):
    logical=False
    x=0
    for o in logical_operators:
        if len(o) == len(a):
            l=x
            length1=len(o)
            while length1>l:
                if o[l] != a[l]:
                    logical=False
                    x=l
                    break
                elif o[l] == a[l]:
                    logical=True
                l=l+1
            if logical == True:
                break
    return logical

def isString(buf):
    strng=False
    if len(buf)>1:
        if buf[0]=="\"":
            if buf[len(buf)-1]=="\"":
                strng=True
        elif buf[0]=="'":
            if buf[len(buf)-1]=="'":
                strng=True
    return strng

def isIdentifier(buf):

    identi=False
    
    x=0
    y=1
    if len(buf) != 0:
        legth1=len(buf)
        
        while True:
            
            
            if ord(buf[x]) >= 65 and ord(buf[x]) <= 90:
                identi=True
            elif ord(buf[x]) >= 97 and ord(buf[x]) <= 122:
                identi=True
            elif ord(buf[x]) >= 48 and ord(buf[x]) <= 57:
                identi=True
            elif ord(buf[x]) == 95:
                identi=True
            if x<legth1:
                break
            else:
                identi=False
                break
            x=x+1
            y=y+1
    return identi
    
    
                    
def isSeparator(a):
    sep=False
    if ord(a)==91 or ord(a)==93 or ord(a)==40 or ord(a)==41 or ord(a)==123 or ord(a)==125 or ord(a)==59 or ord(a)==44 or ord(a)==32:
        sep = True
    return sep

def isTerminal(a):
    
    if a == '$':
        return True

def isSpace(a):
    if a == ' ':
        return True

def isComment(a):
    comm=False
    if a[0]=="#":
        if a[len(a)-1]=="\n":
            comm=True
    return comm

integer=0
string=0
identifier=0
separator=0
oprator=0
logical_operator=0
keyword=0
terminal=0
comment=0


#integer_pattern=re.compile(r"(\+|-)?[0-9]+")
#separator_pattern=re.compile("[(){}|,; ]")
#string_pattern=re.compile(r'(\"([^#\"]|\\.)*\")|(\'([^#\']|\\.)*\')')
#comment_pattern=re.compile(r'\#.*\n')

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

        if isSeparator(a[i]) == True or isTerminal(a[i]) == True or isOperator(a[i])==True or isLogicalOperator(buf)==True or isInteger(a[i])==True or isString(buf)==True:
        
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
                        
            if isLogicalOperator(buf)==True:
                logic=buf+a[i]
                print('Logic '+logic)
                if isLogicalOperator(logic)==True:
                    i=i+1
                    logical_operator=logical_operator+1
                    print('{} is Logical Operator'.format(logic))
                    buf=''
            elif isLogicalOperator(buf)==True:
                logical_operator=logical_operator+1
                print('{} is Logical Operator'.format(buf))
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
            if isSeparator(a[i]):
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
        
        if isSeparator(b[i]) == True or isTerminal(b[i]) == True or isOperator(b[i])==True or isInteger(b[i])==True or isString(buf)==True:
            
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
                logic=buf+b[i]
                print('Logic '+logic)
                if isLogicalOperator(logic)==True:
                    i=i+1
                    logical_operator=logical_operator+1
                    print('{} is Logical Operator'.format(logic))
                    buf=''
            elif isLogicalOperator(buf)==True:
                logical_operator=logical_operator+1
                print('{} is Logical Operator'.format(buf))
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
            if isSeparator(b[i])==True:
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

print("\nNumber of Operators = {}, Number of Keywords = {}, Number of Identifiers = {}, Number of Logical Operators = {}, Number of Integers  = {}, Number of Strings = {}, Number of Separators = {}, Number of Terminals = {}, Number of Comments = {}\n".format(oprator, keyword, identifier, logical_operator, integer, string, separator, terminal, comment))