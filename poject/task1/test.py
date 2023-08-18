import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
from uncertainties import unumpy
from uncertainties import ufloat

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

# Idee: dem dataframe beliebig viele einträge zwischen den gegeben daten mi NaN zu geben -> anschließend interpoloieren zwischen den gegebenen daten
df = []
extra_rows = 150
for i in range(1, 8):
    df.append(pd.read_csv(f'TDK_{i}.csv', comment = '#', header = None ))
    n = extra_rows
    # hier werden die leeren rows angebaut
    new_index = pd.RangeIndex(len(df[i-1])*(n+1))
    new_df = pd.DataFrame(np.nan, index=new_index, columns=df[i-1].columns)
    ids = np.arange(len(df[i-1]))*(n+1)
    new_df.loc[ids] = df[i-1].values
    new_df.interpolate().to_csv("idk.csv")
    df[i-1] = np.array(new_df.interpolate())
    df[i-1][:,3] = np.flip(df[i-1][:,3]/np.max(df[i-1][:,3]))
    df[i-1][:,2] = df[i-1][:,2]*0.5 


##################
##     ENERGYS  ##
##################
# Jetzt eine Maske anglegen die alle werte die > 0.8 sind als true betitelt, die maske anwenden und den letztn wert, da das "rechte" r_max gesucht wird, anwenden 
eps = 0.001
for i in range(0,7):
    plt.plot(df[i][:,2],df[i][:,3])
    mask1 = np.asarray(df[i][:,3]/np.max(df[i][:,3]) > 0.8-eps)
    width = np.flip(np.where(mask1, df[i][:,3], 0).nonzero())
    plt.axvline(x = width[0][0]*0.5/(extra_rows+1) , linestyle  = '--', color = "k")
    print(f"R80 for TDK{i+1}: ", width[0][0]*0.5/(extra_rows+1), "\n -> resulting in an Energy of :", (width[0][0]*0.5/(extra_rows+1)/0.0022)**(1/1.77))
    sigma = 0.012*(width[0][0]*0.5/(extra_rows+1))**0.935 
    unc = ufloat((width[0][0]*0.5/(extra_rows+1)), sigma)
    print(f" -> Error Range: " , unc)
    errorEnergy = (unc/0.0022)**(1/1.77)
    print(f" -> Error Energy: " , errorEnergy)
    print(f" -> relative Energy: " ,    errorEnergy.s *2 /(width[0][0]*0.5/(extra_rows+1)/0.0022)**(1/1.77) *100, "% \n")

#relative energie breite errechnet durch: fehler auf energy *2 / energy in prozent 

plt.axhline(y = 0.8 , linestyle  = '--', color = "k")
#plt.legend()
#plt.show()


