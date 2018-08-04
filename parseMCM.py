from antlr4 import FileStream,CommonTokenStream,ParseTreeWalker
from MCMLexer import MCMLexer
from MCMParser import MCMParser
from EquationListener import EquationListener

def main():
    mcm_file="./mechanism_files/MCM_APINENE.eqn.txt"
    istream=FileStream(mcm_file)
    lexer=MCMLexer(istream)
    tokenstream=CommonTokenStream(lexer)
    parser=MCMParser(tokenstream)
    tree=parser.reactions()
    walker=ParseTreeWalker()
    walker.walk(EquationListener(),tree)

if __name__=='__main__':
    main()