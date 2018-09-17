from antlr4 import *
from gen.MCMParserListener import MCMParserListener
from gen.MCMParser import MCMParser
import scipy.sparse as sparse
import numpy as np
import sys

class EquationListener(MCMParserListener):
    def __init__(self):
        self.eqn_ind=0
        self.chem_ind=0
        #self.chemDict={}
        self.chemOrd={}
        self.mtxInd2Val={}  #num_eqn*num_chem, (eqn_ind,chem_ind)->val
        self.eqnSide=1  #Positive for Reactants, Negative for Productives
        self.spmtx=None

    def enterReaction(self, ctx:MCMParser.ReactionContext):
        self.eqn_ind= int(ctx.IND().getText()) - 1# ZERO INDEXED
        print(f"Parsing Eqn num {self.eqn_ind}", file=sys.stderr)

    def enterReactants(self, ctx:MCMParser.ReactantsContext):
        self.eqnSide=1

    def enterProducts(self, ctx:MCMParser.ProductsContext):
        self.eqnSide=-1

    def enterChemitem(self, ctx:MCMParser.ChemitemContext):
        chem=ctx.CHEM().getText() #[TODO] IGNORE hv
        if ctx.STOI():
            stoi=int(ctx.STOI().getText())
        else:
            stoi=1
        #assert((chem in self.chemDict)==(chem in self.chemOrd))
        #if chem in self.chemDict:
        #    self.chemDict[chem]+=stoi
        #else:
        if not (chem in self.chemOrd):
        #    self.chemDict[chem]=stoi
            self.chemOrd[chem]=self.chem_ind
            self.chem_ind+=1
        if not (self.eqn_ind, self.chemOrd[chem]) in self.mtxInd2Val:
            self.mtxInd2Val[(self.eqn_ind, self.chemOrd[chem])]=0
        else:
            print(f"Discovered duplicated CHEM token: {chem}",file=sys.stderr)
        self.mtxInd2Val[(self.eqn_ind, self.chemOrd[chem])]+= self.eqnSide * stoi

    def exitReactions(self, ctx:MCMParser.ReactionsContext):
        num_eqn=self.eqn_ind+1
        num_chem=self.chem_ind
        print("Generating Sparse matrix",file=sys.stderr)
        self.spmtx=sparse.dok_matrix((num_eqn,num_chem),np.int8)
        for (eqn_ind,chem_ind) in self.mtxInd2Val:
            val=self.mtxInd2Val[(eqn_ind,chem_ind)]
            self.spmtx[eqn_ind,chem_ind]=val
        self.spmtx=self.spmtx.tocsr()
