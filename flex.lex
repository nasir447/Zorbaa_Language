%{
int keywords = 0;
int identifiers = 0;
int operator = 0;
int relational = 0;
int separator = 0;
int terminal = 0;
int integers = 0;
int float1 = 0;
int string = 0;
int comments = 0;
%}

%%
[ \n\t] continue;
\#.*\n {++comments;printf("Comment\n");}
"+"|"="|"+"|"/"|"-"|"!"|"^"|"%" {++operator;printf("Operator = '%s'\n",yytext);}
"<="|">="|"!="|"=="|"<"|">" {++relational;printf("Logical = '%s'\n",yytext);}
"int"|"char"|"float"|"double"|"void"|"bool"|"for"|"while"|"do"|"if"|"else" {++keywords;printf("Keyword = '%s'\n",yytext);}
[(){}|,; ] {++separator;printf("Separator = '%s'\n",yytext);}
[0-9]*"."[0-9]+ {float1++;printf("Float : '%s'\n", yytext);} 
[0-9]+ {integers++; printf("Integer : '%s'\n", yytext);}
\"([^#\"]|\\.)*\" {string++; printf("String = %s\n", yytext);}
\'([^#\']|\\.)*\' {string++; printf("String = %s\n", yytext);}
[a-zA-Z_][a-zA-Z_0-9]* {++identifiers;printf("Identifier = '%s'\n",yytext);}
"$"  {++terminal;printf("Terminal\n");}
End$
%%
int yywrap(void)
{
    return 1;
}
int main(int argc, char **argv)
{
yyin = fopen("Zorbaa.za", "r");
    yylex();
    fclose(yyin);
printf("Number of Operators = %d, Number of Keywords = %d, Number of Identifiers = %d, Number of Logical Operators = %d, Number of Integers  = %d, Number of Floats = %d, Number of Strings = %d Number of Separators = %d, Number of Terminals = %d, Number of Comments = %d\n",
operator, keywords, identifiers, relational, integers, float1, string, separator, terminal);
}
