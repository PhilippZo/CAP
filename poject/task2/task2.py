import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 

df_CTV  = pd.read_csv("../../DoseCTV.csv", header = None, comment  = "#")
df_OAR1 = pd.read_csv("../../DoseOAR1.csv", header = None, comment  = "#")
df_OAR2 = pd.read_csv("../../DoseOAR2.csv", header = None, comment  = "#")
df_Ex = pd.read_csv("../../DoseEx.csv", header = None, comment  = "#")
df_DVH_CTV = pd.read_csv("../../DoseCTV_VolHist.csv", header = None, comment  = "#")

CTV = np.array(df_CTV)
OAR1 = np.array(df_OAR1)
OAR2 = np.array(df_OAR2)
Ex = np.array(df_Ex)
DVH_CTV = np.array(df_DVH_CTV)

plt.plot(DVH_CTV[:,0], DVH_CTV[:,1])
plt.show()
plt.clf()

CTV_x = np.zeros(512)
CTV_y = np.zeros(512)
CTV_z = np.zeros(81)

OAR1_x = np.zeros(512)
OAR1_y = np.zeros(512)
OAR1_z = np.zeros(81)

OAR2_x = np.zeros(512)
OAR2_y = np.zeros(512)
OAR2_z = np.zeros(81)

Ex_x = np.zeros(512)
Ex_y = np.zeros(512)
Ex_z = np.zeros(81)


for i in range(81):
    CTV_z[i] = np.sum(CTV[i::81,3])
    OAR1_z[i] = np.sum(OAR1[i::81,3])
    OAR2_z[i] = np.sum(OAR2[i::81,3])
    Ex_z[i] = np.sum(Ex[i::81,3])

for i in range(512):
    for j in range(512):
        CTV_x[i]  = CTV_x[i] + np.sum(CTV[:,3][j*512*81+81*i:j*512*81+81+81*i])
        CTV_y[i] = CTV_y[i] + np.sum(CTV[:,3][j*81+81*512*i:j*81+81+81*512*i])
        OAR1_x[i] = OAR1_x[i] + np.sum(OAR1[:,3][j*512*81+81*i:j*512*81+81+81*i])
        OAR1_y[i] = OAR1_y[i] + np.sum(OAR1[:,3][j*81+81*512*i:j*81+81+81*512*i])
        OAR2_x[i] = OAR2_x[i] + np.sum(OAR2[:,3][j*512*81+81*i:j*512*81+81+81*i])
        OAR2_y[i] = OAR2_y[i] + np.sum(OAR2[:,3][j*81+81*512*i:j*81+81+81*512*i])
        Ex_x[i] = Ex_x[i] + np.sum(Ex[:,3][j*512*81+81*i:j*512*81+81+81*i])
        Ex_y[i] = Ex_y[i] + np.sum(Ex[:,3][j*81+81*512*i:j*81+81+81*512*i])


plt.plot(CTV[0:81,2], CTV_z, label ="CTV")      
plt.plot(CTV[0:81,2], OAR1_z,label ="OAR1")     
plt.plot(CTV[0:81,2], OAR2_z,label ="OAR2")      
plt.plot(CTV[0:81,2], Ex_z,  label ="External")
plt.title("z axis")
plt.legend()
plt.show()
plt.clf()

plt.plot(CTV[0::81,1][0:512], CTV_x ,"k-", label ="CTV"     )
plt.plot(CTV[0::81,1][0:512], OAR1_x,"b-", label ="OAR1"    )
plt.plot(CTV[0::81,1][0:512], OAR2_x,"r-", label ="OAR2"    )
plt.plot(CTV[0::81,1][0:512], Ex_x,  "y-", label ="External")
plt.title("x axis")
plt.legend()
plt.show()
plt.clf()


plt.plot(CTV[0::81,1][0:512], CTV_y ,"k-", label ="CTV"     )
plt.plot(CTV[0::81,1][0:512], OAR1_y,"b-", label ="OAR1"    )
plt.plot(CTV[0::81,1][0:512], OAR2_y,"r-", label ="OAR2"    )
plt.plot(CTV[0::81,1][0:512], Ex_y,  "y-", label ="External")
plt.title("y axis")
plt.legend()
plt.show()
plt.clf()
