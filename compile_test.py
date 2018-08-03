import os
#first install antlr4-python: pip install antlr4-python3-runtime
if not ("CLASSPATH" in os.environ):
    os.environ["CLASSPATH"]=""
os.environ["CLASSPATH"]=os.path.abspath("./antlr/antlr-4.7.1-complete.jar")+";"+os.environ["CLASSPATH"]
files=["MCMLexer.g4","MCMParser.g4"]
for f in files:
    os.system(f"java org.antlr.v4.Tool -Dlanguage=Python3 {f}")
os.system(f"python ./antlr/pygrun MCM reactions --tokens ./mechanism_files/MCM_APINENE.eqn.txt > tokens.txt")
os.system(f"python ./antlr/pygrun MCM reactions --tree ./mechanism_files/MCM_APINENE.eqn.txt > ast.txt")