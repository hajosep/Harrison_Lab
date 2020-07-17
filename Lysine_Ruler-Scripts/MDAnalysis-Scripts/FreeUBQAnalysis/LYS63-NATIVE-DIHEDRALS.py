
# coding: utf-8

# In[1]:


import MDAnalysis as mda
import pandas as pd
import numpy as np
from MDAnalysis.analysis.dihedrals import Dihedral
from MDAnalysis.analysis.dihedrals import Ramachandran


# In[2]:

# In[3]:


u = mda.Universe('UBQ-WB.psf','UBQ-WB-Run4-2fs-25MIL-V2.dcd')


# In[4]:


#for i in u.residues:
   # print(i)
#63 remains CYS


# In[4]:


MutResi = u.residues[62]


# In[5]:


MutAtoms = u.select_atoms('(resname CYS)')


# In[6]:


CH1 = ['N','CA','CB','CG']
CH2 = ['CA','CB','CG','CD']
CH3 = ['CB','CG','CD','CE']
CH4 = ['CG','CD','CE','NZ']
#CH5 = ['CD','CE','C6','NZ']


# In[7]:


def AtomPull(chilist):
    Sele = 'resid 63 and ('
    for item in chilist:
        Sele += 'name '
        Sele += item
        Sele += ' or '
    Sele = Sele[:-4]
    Sele += ')'
    Selection = u.select_atoms(Sele)
    return Selection


# In[8]:


PHI = MutResi.phi_selection()
PSI = MutResi.psi_selection()
CHI1 = AtomPull(CH1)
CHI2 = AtomPull(CH2)
CHI3 = AtomPull(CH3)
CHI4 = AtomPull(CH4)
#CHI5 = AtomPull(CH5)
FullSet = [PHI,PSI,CHI1,CHI2,CHI3,CHI4]
#FullSet = [PHI,PSI,CHI1]


# In[9]:


for item in FullSet:
    print(len(item))


# In[10]:


PhiCalc = mda.analysis.dihedrals.Dihedral(FullSet).run()


# In[11]:


def CSVReporter(array):
    CSV = pd.DataFrame()
    Row = 0
    for angleset in array:
        CSV.at[Row,'Phi'] = angleset[0]
        CSV.at[Row,'Psi'] = angleset[1]
        CSV.at[Row,'Chi1'] = angleset[2]
        CSV.at[Row,'Chi2'] = angleset[3]
        CSV.at[Row,'Chi3'] = angleset[4]
        CSV.at[Row,'Chi4'] = angleset[5]
        #CSV.at[Row,'Chi5'] = angleset[6]
        Row += 1
    return CSV
        


# In[12]:


CSVReporter(PhiCalc.angles).to_csv('K63NativeAngles.csv')

