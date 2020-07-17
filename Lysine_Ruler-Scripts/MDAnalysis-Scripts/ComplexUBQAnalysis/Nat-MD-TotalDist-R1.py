
# coding: utf-8

import MDAnalysis as mda
import pandas as pd
import numpy as np
from MDAnalysis.analysis.dihedrals import Dihedral
from MDAnalysis.analysis.dihedrals import Ramachandran
from MDAnalysis.analysis import distances

u = mda.Universe('Ros-TC_NeutralLYS-Jones-125WB.psf','THIOCOMPLEX-RosTC-Native-Jones-WB12p5A-Run1-2fs-12point5MIL.dcd')
CurrDF = pd.DataFrame()

D116O1 = u.select_atoms('resid 116 and resname ASP and name OD1')
D116O2 = u.select_atoms('resid 116 and resname ASP and name OD2')
G76C = u.select_atoms('resid 222 and resname GLY and name C')
K63N = u.select_atoms('segid EP1 and resid 285 and name NZ')
G76O = u.select_atoms('resid 222 and resname GLY and name OT1')
N76N = u.select_atoms('resid 76 and resname ASN and name ND2 and segid AP1')

Set = [D116O1,D116O2,G76C,K63N,G76O,N76N]
print(Set)
for item in Set:
    print(item)

def DistFullDF(AtomPairList,CurrDF,NameList):
    Row = 0
    for ts in u.trajectory:
        PairID = 0
        for Pair in AtomPairList:
            Val = mda.analysis.distances.dist(Pair[0],Pair[1])
            CurrDF.at[Row,'Frame'] = Row
            CurrDF.at[Row,'Distance'] = Val[2][0]
            CurrDF.at[Row,'DistType'] = NameList[PairID]
            PairID += 1
            Row += 1
            if(Row % 1000 == 0):
                print(Row)
    return CurrDF

APList = [[G76C,K63N],[D116O1,K63N],[D116O2,K63N],[G76O,K63N],[G76O,N76N]]
NameList = ['G76C-K63N','D116O1-K63N','D116O2-K63N','G76O-K63N','G76O-N76N']

CurrDF = DistFullDF(APList,CurrDF,NameList)

# In[40]:
CurrDF.to_csv('Ros-NH2-C4-R1-Jones-DistSet.csv')