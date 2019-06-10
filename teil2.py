import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from uncertainties import ufloat
import uncertainties.unumpy as unp
m = np.array([0.009 , 0.0141, 0.0151 , 0.0079]) 
l = 0.135
r = np.array([7240, 7400, 7800, 6260])
q = (m)/(r * l)
print(q)
F = 8.66 * 10**(-5)
R3 = 998
Us = 500
theo = np.array([0.003, 0.014, 0.025, 0.001])
def csv_read(pathToFile, delimiter=";"):
    with open(pathToFile, "r") as f:
        content = []
        for line in f:
            content.append((line.rstrip()).split(delimiter))
    return content


print("       ****          ")
werte = csv_read("csv/Nd2O3.csv")
Rdata = np.zeros(3)
Udata = np.zeros(3)
ignore = True
i=0
for values in werte:
    if(ignore):
        ignore = False
    else:
        Rdata[i] = float(values[4])
        Udata[i] = float(values[5]) 
        i+=1
R = ufloat(np.mean(Rdata), np.std(Rdata, ddof=1) / np.sqrt(len(Rdata)))   
U = ufloat(np.mean(Udata), np.std(Udata, ddof=1) / np.sqrt(len(Udata)))  
xr = 2 * R * F /(R3 * q[0])   
xu = 4 * F * U / (q[0] * Us)  

print("R", R)
print("U", U)
print("xr", xr)
print("xu", xu)
ar = (theo[0] - xr)/(theo[0]) *100
au = (theo[0] - xu)/(theo[0]) *100
print("ar", ar)
print("au", au)
print("       ****          ")

###########

werte = csv_read("csv/Gd2O3.csv")
Rdata = np.zeros(3)
Udata = np.zeros(3)
ignore = True
i=0
for values in werte:
    if(ignore):
        ignore = False
    else:
        Rdata[i] = float(values[4])
        Udata[i] = float(values[5]) 
        i+=1
           
R = ufloat(np.mean(Rdata), np.std(Rdata, ddof=1) / np.sqrt(len(Rdata)))   
U = ufloat(np.mean(Udata), np.std(Udata, ddof=1) / np.sqrt(len(Udata)))  
xr = 2 * R * F /(R3 * q[1])    
xu = 4 * F * U / (q[1] * Us)  
print("R", R)
print("U", U)
print("xr", xr)
print("xu", xu)
ar = (theo[1] - xr)/(theo[1]) *100
au = (theo[1] - xu)/(theo[1]) *100
print("ar", ar)
print("au", au)
print("       ****          ")
###############
werte = csv_read("csv/Dy2O3.csv")
Rdata = np.zeros(3)
Udata = np.zeros(3)
ignore = True
i=0
for values in werte:
    if(ignore):
        ignore = False
    else:
        Rdata[i] = float(values[4])
        Udata[i] = float(values[5]) 
        i+=1
     
R = ufloat(np.mean(Rdata), np.std(Rdata, ddof=1) / np.sqrt(len(Rdata)))   
U = ufloat(np.mean(Udata), np.std(Udata, ddof=1) / np.sqrt(len(Udata)))  
xr = 2 * R * F /(R3 * q[2])   
xu = 4 * F * U / (q[2] * Us)  
print("R", R)
print("U", U)
print("xr", xr)
print("xu", xu)
ar = (theo[2] - xr)/(theo[2]) *100
au = (theo[2] - xu)/(theo[2]) *100
print("ar", ar)
print("au", au)
print("       ****          ")

#########
werte = csv_read("csv/C6O12Pr2.csv")
Rdata = np.zeros(3)
Udata = np.zeros(3)
ignore = True
i=0
for values in werte:
    if(ignore):
        ignore = False
    else:
        Rdata[i] = float(values[4])
        Udata[i] = float(values[5]) 
        i+=1
           
R = ufloat(np.mean(Rdata), np.std(Rdata, ddof=1) / np.sqrt(len(Rdata)))   
U = ufloat(np.mean(Udata), np.std(Udata, ddof=1) / np.sqrt(len(Udata)))  
xr = 2 * R * F /(R3 * q[3])    
xu = 4 * F * U / (q[3] * Us)  
print("R", R)
print("U", U)
print("xr", xr)
print("xu", xu)
ar = (theo[3] - xr)/(theo[3]) *100
au = (theo[3] - xu)/(theo[3]) *100
print("ar", ar)
print("au", au)
print("       ****          ")
#######
