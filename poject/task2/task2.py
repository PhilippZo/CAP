import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 

df_CTV = pd.read_csv("../../DoseCTV.csv", header = None, comment  = "#")

CTV = np.array(df_CTV)

plt.plot(CTV[:,2], CTV[:,3])