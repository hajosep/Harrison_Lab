import MDAnalysis as mda
from MDAnalysis.analysis.rms import RMSF,RMSD
from MDAnalysis.analysis import align, rms
import pandas as pd
import numpy as np

K63MOBILE = mda.Universe('1UBQ-C5-63-WB.psf','UBQ-MUT-CHARGE-CRNG-RunX-2fs-25MIL-298K.dcd')
K63REF = mda.Universe('1UBQ-C5-63-WB.psf','UBQ-MUT-CHARGE-CRNG-RunX-2fs-25MIL-298K.dcd')
K63REF.trajectory[0]
K63Align = align.AlignTraj(K63MOBILE,K63REF, select = 'protein', filename = 'K63-FFAlign.dcd').run()
K63Aligned = mda.Universe('1UBQ-C5-63-WB.psf','K63-FFAlign.dcd')


K63atoms = K63Aligned.select_atoms('protein and name CA')
K63rmsder = RMSD(K63atoms, verbose = True).run()


np.savetxt("K63-RMSD.csv", K63rmsder.rmsd, delimiter=",")

