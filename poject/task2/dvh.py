import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 

df = pd.read_csv("test.csv", header = 1)
dvh = np.array(df)


fig, ax = plt.subplots()
x = np.linspace(0,15)

ax.plot(dvh[:,0], dvh[:,1], label = "CTV")
ax.plot(dvh[:,0], dvh[:,3], label = "External")
ax.plot(dvh[:,0], dvh[:,5], label = "OAR1")
ax.plot(dvh[:,0], dvh[:,7], label = "OAR2")

ax.fill_between(x,0,10, alpha = 0.6,  label = "OAR safety regime")
ax.axvline(x = 15, alpha = 0.5, color = "black", linestyle = "--")
ax.axhline(y = 10, alpha = 0.5, color = "black", linestyle = "--")
#ax.plot(60*0.95, alpha = 0.5, color = "black", linestyle = "--" , label = "95% of wanted Dose")

ax.set_xlabel("Dose [Gy]")
ax.set_ylabel("relativ Volume")

plt.title("Dose Volume Histogram")
plt.grid()
plt.legend()
plt.savefig("DVH.pdf")