from antlr4 import FileStream,CommonTokenStream,ParseTreeWalker
from gen.MCMLexer import MCMLexer
from gen.MCMParser import MCMParser
from visitors.EquationListener import EquationListener

def parseMCM():
    mcm_file="./mechanism_files/MCM_APINENE.eqn.txt"
    istream=FileStream(mcm_file)
    lexer=MCMLexer(istream)
    tokenstream=CommonTokenStream(lexer)
    parser=MCMParser(tokenstream)
    tree=parser.reactions()
    walker=ParseTreeWalker()
    listener=EquationListener()
    walker.walk(listener,tree)
    return listener

if __name__=='__main__':
    listener=parseMCM()