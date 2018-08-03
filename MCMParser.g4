parser grammar MCMParser;
options { tokenVocab=MCMLexer; }

reactions: (reaction NEWLINE?)+;
reaction: LPARA IND RPARA eqn COLON rate SEMICOLON;
eqn: reactants EQUAL products;
reactants: chemitem ( CHEMPLUS chemitem)* ;
products: chemitem ( CHEMPLUS chemitem)* ;
chemitem: CHEM #Chem
        | STOI CHEM #StoiChem
        ;
rate: rate_expr;
rate_expr: LP rate_expr RP
         | <assoc=right> rate_expr POW rate_expr
         | rate_expr op=(MULT | DIV ) rate_expr
         | rate_expr op=(PLUS | MINUS) rate_expr
         | MINUS rate_expr
         | JVEC
         | DOUBLE | FLOAT | INT
         | VAR
         | EXP LP rate_expr RP
         ;
//num: DOUBLE | FLOAT | INT;
//int_num: DIGIT+;
//float_num: int_num DOT int_num?;
//double_num: float_num D (PLUS | MINUS)? int_num;
