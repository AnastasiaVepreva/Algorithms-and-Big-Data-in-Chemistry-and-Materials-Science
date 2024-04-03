import pandas as pd
import numpy as np
from rdkit import Chem

df = pd.read_csv('vepreva_dataset.csv')

smiles = df['smiles'].to_list()

mols = [Chem.MolFromSmiles(i) for i in smiles]
MorganFP = []
header = ['bit' + str(i) for i in range(2048)]
for i in range(len(mols)):
    fps = list(Chem.RDKFingerprint(mols[i]).ToBitString())
    MorganFP.append(fps)
df2 = pd.DataFrame(MorganFP,columns=header)
df2.insert(loc=0, column='smiles', value=smiles)
print(df2) 
