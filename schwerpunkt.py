import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

df_p = pd.read_csv("P.csv", header = None, comment = "#")
df_pprim = pd.read_csv("Pprim.csv", header = None, comment = "#")

df_c = pd.read_csv("C.csv", header = None, comment = "#")
df_cprim = pd.read_csv("Cprim.csv", header = None, comment = "#")


proton = np.array(df_p) #/np.max(np.array(df_p))
proton_prim = np.array(df_pprim) #/np.max(np.array(df_p))

carbon = np.array(df_c) #/np.max(np.array(df_c))
carbon_prim = np.array(df_cprim) #/np.max(np.array(df_c))


plt.plot(proton[:,2], proton[:,3])
plt.plot(carbon[:,2], carbon[:,3])
plt.plot(proton_prim[:,2], proton_prim[:,3], label = "primaries")
plt.plot(carbon_prim[:,2], carbon_prim[:,3], label = "primaries")

plt.legend()
plt.show()