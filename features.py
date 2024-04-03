import pandas as pd
import numpy as np

df = pd.read_csv('qm9.csv')

random = df.sample(n = 20000, random_state = 2)

random.to_csv('vepreva_dataset.csv', index=True)
