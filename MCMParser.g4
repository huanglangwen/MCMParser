parser grammar MCMParser;
options { tokenVocab=MCMLexer; }

reactions: (reaction NEWLINE?)+;
reaction: LPARA IND DOT? RPARA eqn COLON rate SEMICOLON;
eqn: reactants EQUAL products;
reactants: chemitem ( CHEMPLUS chemitem)* ;
products: chemitem ( CHEMPLUS chemitem)* ;
chemitem: STOI? CHEM;

rate: rate_expr;
rate_expr: LP rate_expr RP #Parens
         | <assoc=right> rate_expr POW rate_expr #Pow
         | rate_expr op=(MULT | DIV ) rate_expr #MultDiv
         | rate_expr op=(PLUS | MINUS) rate_expr #PlusMinus
         | MINUS rate_expr #Negative
         | JVEC #Jvec
         | (DOUBLE | FLOAT | INT) #Num
         | VAR #Var
         | EXP LP rate_expr RP #Exp
         ;
//num: DOUBLE | FLOAT | INT;
//int_num: DIGIT+;
//float_num: int_num DOT int_num?;
//double_num: float_num D (PLUS | MINUS)? int_num;
