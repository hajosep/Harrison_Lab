
# coding: utf-8

# In[ ]:


import MDAnalysis as mda
import pandas as pd
import numpy as np
from MDAnalysis.analysis.dihedrals import Dihedral
from MDAnalysis.analysis.dihedrals import Ramachandran
from MDAnalysis.analysis import distances


# In[ ]:


u = mda.Universe('UBQ-WB.psf','UBQ-WB-Run4-2fs-25MIL-V2.dcd')


# In[ ]:


def DistDF(Atom1,Atom2):
    CurrDF = pd.DataFrame()
    Row = 0
    for ts in u.trajectory:
        Val = mda.analysis.distances.dist(Atom1,Atom2)
        CurrDF.at[Row,'Frame'] = Row
        CurrDF.at[Row,'Distance'] = Val[2][0]
        Row += 1
        if(Row % 1000 == 0):
            print(Row)
    return CurrDF


# In[ ]:


NTerm = u.select_atoms('resname LYS and resid 63 and name NZ')


# In[ ]:


CA = u.select_atoms('resid 63 and resname LYS and name CA')


# In[ ]:


CANDF = DistDF(CA,NTerm)


# In[ ]:


CANDF.to_csv('K63N-DISTDF-Run1.csv')

