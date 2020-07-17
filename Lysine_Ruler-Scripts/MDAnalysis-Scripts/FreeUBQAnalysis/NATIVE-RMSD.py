import MDAnalysis as mda
from MDAnalysis.analysis.rms import RMSF,RMSD
from MDAnalysis.analysis import align, rms
import pandas as pd
import numpy as np

#K11Align = align.AlignTraj(K11MOBILE,K11REF, select = 'protein', filename = 'K11-FFAlign.dcd').run()
K63Aligned = mda.Universe('UBQ-WB.psf','NATIVE-FFAlign.dcd')


K63atoms = K63Aligned.select_atoms('protein and name CA')
K63rmsder = RMSD(K63atoms, verbose = True).run()


np.savetxt("NATIVE-RMSD.csv", K63rmsder.rmsd, delimiter=",")

