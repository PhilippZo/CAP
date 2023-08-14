import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 


###############################
######     TASK 1 a)    #######
###############################

df  = pd.read_csv('Profil_150MeV.csv', comment = '#', header = None )
task1 = np.array(df)
task1[:,3] = task1[:,3]/np.max(task1[:,3])
task1[:,0] = task1[:,0]*0.05-2


eps = 0.01
mask1 = np.asarray(task1[:,3] > 0.5-eps)
mask2 = np.asarray(task1[:,3] < 0.5+eps)

width = np.where(mask1, task1[:,3], 0)
width = np.where(mask2,width, 0).nonzero()

print("fist 50% at: ", width[0][0]*0.05 -2,"  second 50% at: ", width[0][1]*0.05-2 )


#plot with lines 
plt.plot(task1[:,0], task1[:,3])
plt.axvline(x = width[0][0]*0.05 -2, linestyle  = '--', color = "k")
plt.axvline(x = width[0][1]*0.05 -2, linestyle  = '--', color = "k")
plt.grid()
plt.xlabel('width [cm]')
plt.ylabel('')
plt.title('Relative Tiefendosiskurve als Verhältnis')
#plt.savefig('task1a.pdf')
plt.clf()



###############################
######     TASK 1 b)    #######
###############################
df = np.zeros((8,80, 4))
for i in range(1, 8):
    df[i] =  np.array(pd.read_csv(f'TDK_{i}.csv', comment = '#', header = None ))
    df[i][:,3] = np.flip(df[i][:,3]/np.max(df[i][:,3]))
    df[i][:,2] = df[i][:,2]*0.5 + 0.5

eps = 0.2
for i in range(1,8):
    plt.plot(df[i][:,2],df[i][:,3])
    mask1 = np.asarray(df[i][:,3]/np.max(df[i][:,3]) == 1)
    width = np.flip(np.where(mask1, df[i][:,3], 0).nonzero())
    plt.axvline(x = width[0][0]*0.5 + 0.5 , linestyle  = '--', color = "k")
    print(f"R80 for TDK{i}: ", width[0][0]*0.5+0.5)
    
#plt.legend()
plt.show()
