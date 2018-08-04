lexer grammar MCMLexer;

WS: [ \t]+ -> channel(HIDDEN) ; 
LPARA : '{' -> pushMode(INDMODE);
NEWLINE : ('\r'? '\n')+ ;

mode INDMODE;
DOT: '.';
IND: [1-9][0-9]*;
RPARA: '}' -> mode(EQNMODE);

mode EQNMODE;
CHEM: [A-Z][0-9A-Z]*;
STOI: [1-9][0-9]*;
CHEMPLUS: '+';
EQUAL: '=';
COLON : ':' -> mode(RATEMODE);
WSEQN: [ \t]+ -> channel(HIDDEN) ;

mode RATEMODE;
fragment DIGIT: [0-9];
//D: 'D';
//DOT: '.';
DOUBLE: DIGIT+ '.'? DIGIT* 'D' [+\-]? DIGIT+;
FLOAT: DIGIT+ '.' DIGIT*;
INT: [1-9] DIGIT*;
WSRATE: [ \t]+ -> channel(HIDDEN);
//NUM: DOUBLE | FLOAT | INT;
JVEC: 'J(' [1-9] DIGIT* ')';
POW: '**';
MULT: '*';
DIV: '/';
PLUS: '+';
MINUS: '-';
EXP: 'EXP';
LP: '(';
RP: ')';
VAR: [A-Z][0-9A-Z]*;
//RATE: ~[ :;{}]((~[:;{}])*~[ :;{}])?;
SEMICOLON: ';'->popMode;








