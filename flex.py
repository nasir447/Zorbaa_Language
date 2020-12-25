import re

integer=0
string=0
float1=0
identifier=0
separator=0
oprator=0
logical_operator=0
keyword=0
terminal=0

identifier_pattern=re.compile("[A-Za-z_][A-Za-z0-9_]*")
integer_pattern=re.compile("[0-9]+")
separator_pattern=re.compile("[(){}|,; ]")
float_pattern=re.compile('[0-9]*.[0-9]+')
string_pattern=re.compile(r'\"(.+?)\"')

f = open("Zorbaa.za", "r")
operators=['+','-','/','*','=','!','|','%']
logical_operators=["<=",">=","!=","==","<",">"]
keywords=["int","char","float","double","void","bool","for","while","do","if","else"]

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
        
        if a[i]==' ' or a[i] == '$':
            
            for key in keywords:
                if key == buf:
                    keyword=keyword+1
                    print('{} is Keyword'.format(buf))
                    buf=''
                    break

            for o in operators:
                if o == buf:
                    oprator=oprator+1
                    if buf == o:
                        print('{} is Operator'.format(buf))
                        buf=''
                        break

            for o in logical_operators:
                if buf == o:
                    logical_operator=logical_operator+1
                    print('{} is Logical Operator'.format(buf))
                    buf=''
                    break
            
            if float_pattern.fullmatch(buf) is not None:
                float1=float1+1
                print('{} is Float'.format(buf))
                buf=''
            
            if integer_pattern.fullmatch(buf) is not None:
                integer=integer+1
                print('{} is Integer'.format(buf))
                buf=''

            if string_pattern.fullmatch(buf) is not None:
                string=string+1
                print('{} is String'.format(buf))
                buf=''

            if identifier_pattern.fullmatch(buf) is not None:
                identifier=identifier+1
                print('{} is Identifier'.format(buf))
                buf=''

            if a[i] == '$':
                terminal=terminal+1
                print('Terminal')
                buf=''

            buf=''
               
        if a[i] != ' ':       
            buf+=a[i]
            if separator_pattern.fullmatch(buf) is not None:
                separator=separator+1
                print('{} is Separator'.format(buf))
                buf=''

        i+=1
        if i >= length:
            break
    
    if not b:
        break
    length=len(b)
    i=0
    buf=""
    while True:
        if not b:
            break
        
        if b[i]==' ' or b[i] == '$':
            for key in keywords:
                if key == buf:
                    keyword=keyword+1
                    print('{} is Keyword'.format(buf))
                    buf=''
                    break

            for o in logical_operators:
                if buf == o:
                    logical_operator=logical_operator+1
                    print('{} is Logical Operator'.format(buf))
                    buf=''
                    break

            for o in operators:
                if buf == o:
                    oprator=oprator+1
                    print('{} is Operator'.format(buf))
                    buf=''
                    break
            
            if float_pattern.fullmatch(buf) is not None:
                float1=float1+1
                print('{} is Float'.format(buf))
                buf=''

            if integer_pattern.fullmatch(buf) is not None:
                integer=integer+1
                print('{} is Integer'.format(buf))
                buf=''

            if string_pattern.fullmatch(buf) is not None:
                string=string+1
                print('{} is String'.format(buf))
                buf=''
            
            if identifier_pattern.fullmatch(buf) is not None:
                identifier=identifier+1
                print('{} is Identifier'.format(buf))
                buf=''

            if b[i] == '$':
                terminal=terminal+1
                print('Terminal')
                buf=''

            buf=''
               
        if b[i] != ' ':       
            buf+=b[i]
            if separator_pattern.fullmatch(buf) is not None:
                separator=separator+1
                print('{} is Separator'.format(buf))
                buf=''

        i+=1
        if i >= length:
            break
    
f.close()

print("Number of Operators = {}, Number of Keywords = {}, Number of Identifiers = {}, Number of Logical Operators = {}, Number of Integers  = {}, Number of Floats = {}, Number of Strings = {}, Number of Separators = {}, Number of Terminals = {}\n".format(oprator, keyword, identifier, logical_operator, integer, float1, string, separator, terminal))