#flex using python for Zorbaa Language
#
#Name: Nasir Khalil
#Roll Number: cs181005
#date: 28*12*2020





#import re

def isOperator(a):
    #according to dfa logic either any operator will match or not, if it will not match it goes to reject state
    #and here if any operator in all operators in "operators" list dont match it will return false, 
    # which represents reject state 
    for o in operators:
        if o == a:
            return True
    return False

def isInteger(a):
    intiger_bool=False
    # checking of integer according to dfa is quite simple 
    
    if len(a)!=0:
    #at first we check that either a has some value or is it empty
    # if it is empt, we will simply return intiger_bool which is flse
    # indicating a reject state    
        if ord(a[0])==45:
            #then we check for signed integers that weather it contains "-" or not
            x=1;
            length1=len(a)
            #then we check the length of integer, here x is initialixed with  because at  position ther is "-" sign
            while x<length1:
                #then we started loop and we are checking character by character or state by state
                # just like dfa
                if ord(a[x])>=48 and ord(a[x])<=57:
                    intiger_bool=True
                else:
                    #if there are values that are not in between 0-9
                    #just like dfa it will reject th entire string and
                    #return false
                    intiger_bool=False
                    break
                x=x+1
        else:
            #this is for unsigned integers
            x=0;
            length1=len(a)
            while x<length1:
                #then we started loop and we are checking character by character or state by state
                # just like dfa
                if ord(a[x])>=48 and ord(a[x])<=57:
                    intiger_bool=True
                else:
                    #if there are values that are not in between 0-9
                    #just like dfa it will reject th entire string and
                    #return false
                    intiger_bool=False
                    break
                x=x+1
    
    return intiger_bool


def isKeyWord(a):
    #the real logic is here
    iskey =False
    #a bool to return initialized as false
    x=0
    #it is simply a variable used for iteration purpose
    for key in keywords:
        #there is a small list globally defined named keywords, from list we are
        #getting a keyword in each iteration named as "key"
        if len(key) == len(a):
            #now only that key ords will be selected from keywords list which
            # have the same length, suppose I want "char", length 4 keywords will be selected only
            # from which are present in keywords list  
            o=x
            #this line is very important, remember x is declared above and given 0 and now o is initialized with whatever x is
            length1=len(key)
            #we took length of key for loop iteration
            #suppose we need "void" as tocken mapped as keyword
            #now suppose we have "keywords" list as ["vool"(it is not a keyword,just for explaining what is happening here), "void"]
            #now, if we apply dfa machine what will happen is that it will check for "v", both will have "v" so state will be incremented
            #then it will check for "o" and that will match too, state will be incremented again,
            #now there will be a position where the decision is needed, there will be two stated one for "o" and one for "i",
            #rest will be going toward reject, here exactly that is happening
            while length1>o:
                if key[o] != a[o]:
                    #letters stop matching, it is th decision point
                    iskey=False
                    #bool for return is set to false
                    x=o
                    #here "x" is given the value of "o" which till "o" length the given keyword is accepted and now check it from further it
                    # remember we have intitiaized "o" wi "x" above. 
                    break
                elif key[o] == a[o]:
                    #we will check if the letters are same we will give te value of true to the bool to return
                    iskey=True
                o=o+1
                #variable for iteration is incremented
            if iskey == True:
                #if key word is succesfully mapped, break the loop
                break
    #bool for return
    return iskey

#SAME LOGIC AS OF KEYWORDS
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
            #for string constant to check w checked either the first letter is " just like dfa 
            # if " comes then we dont care what comes next, until " comes, like (a+b)* in dfa
            if buf[len(buf)-1]=="\"":
                #here it is checked and bool for return is set to true
                strng=True
        elif buf[0]=="'":
            #same thing as above done for single wuotation
            if buf[len(buf)-1]=="'":
                strng=True
    return strng

def isIdentifier(buf):
    #to check for identifiers
    identi=False
    x=0
    if len(buf) != 0:
        legth1=len(buf)
        #length of given identifire to check is recorded
        while True:
            #loop for iteration started
            if ord(buf[x]) >= 65 and ord(buf[x]) <= 90:
                #checking weather the letter of identifier to check is between A-Z or not 
                identi=True
            elif ord(buf[x]) >= 97 and ord(buf[x]) <= 122:
                #checking weather the letter of identifier to check is between a-z or not
                identi=True
            elif ord(buf[x]) >= 48 and ord(buf[x]) <= 57:
                #checking weather the letter of identifier to check is between 0-9 or not
                identi=True
            elif ord(buf[x]) == 95:
                #checking weather the letter of identifier to check is "_" or not
                identi=True
            if x<legth1:
                break
            else:
                #if not we go into reject state which means returning false
                identi=False
                break
            x=x+1
            
    return identi
    
    
                    
def isSeparator(a):
    sep=False
    if ord(a)==91 or ord(a)==93 or ord(a)==40 or ord(a)==41 or ord(a)==123 or ord(a)==125 or ord(a)==59 or ord(a)==44 or ord(a)==32:
        #it is simply checing for seperators like "[", "]", "{", "}", "(", ")", ";", ",", " "
        sep = True
    #if not true that means rejected and it returns default value of false from function
    return sep

def isTerminal(a):
    #it is a simple funtion which is telling us weather terminal "$" occured, which can also be mapped on dfa easily
    if a == '$':
        return True
    else:
        return False

def isSpace(a):
    #SAME LOGIC AS OF TERMINAL
    if a == ' ':
        return True
    else:
        return False

def isComment(a):
    #SAME LOGIC AS OF TERMINAL
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
#some global variables

f = open("Zorbaa.za", "r")
operators=['+','-','/','*','=','!','|','%']
logical_operators=["<=",">=","!=","==","<",">"]
keywords=["int","char","float","double","void","bool","for","while","do","if","else","print","input","return","fun","true","false"]

while True:
    a=f.readline()
    b=f.readline()
    #two buffers "a" and "b" have one line each from file
    if not a:
        #to check a is not null
        break
    length=len(a)
    #took length of a for iterations
    i=0
    buf=""
    while True:
        if not a:
            break
        #here it is checked that weather separator or trminal or operator or logical operator or integer or string has occured.
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
            #this is the place whare space is separated from buffer
            buf+=a[i]
            if isSeparator(a[i]):
                separator=separator+1
                print('{} is Separator'.format(buf))
                buf=''

        i+=1
        if i >= length:
            if isComment(buf):
                #comment is checked here
                comment=comment+1
                print("Comment")
            break
    
    if not b:
        #SAME PROCESS AS OF A IS DONE FOR B FOR 2 BUFFERS
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
#final print statement