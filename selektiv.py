import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def csv_read(pathToFile, delimiter=";"):
    with open(pathToFile, "r") as f:
        content = []
        for line in f:
            content.append((line.rstrip()).split(delimiter))
    return content

def func(x, a, b, c):
    return a/( (x**2 - c**2)**2 + b**2 * c**2)
def funcs(x):
    return 100/np.sqrt(2)

#nullmessung = 829 / 900

werte = csv_read("csv/selektiv.csv")
xdata = np.zeros(39)
ydata = np.zeros(39)



ignore = True
i=0
for values in werte:
    if(ignore):
        ignore = False
    else:
        xdata[i] = float(values[0])
        ydata[i] = float(values[1]) 
        i+=1

guess = [ -0.7, 66000, 35]
x_line = np.linspace(20, 40, 5000)
pxdata = xdata[14:35]
pydata = ydata[14:35]
print(pxdata)
plt.plot(xdata, ydata, "rx", label="Messwerte")
popt, pcov = curve_fit(func, pxdata, pydata)
plt.plot(x_line, func(x_line, *popt), "b-", label="Fit")
plt.hlines(110/np.sqrt(2), xmin=20, xmax =40)
#µ = (1.03 \pm 0.02)
#\ln ( N_ 0 ) = 5.05 \pm 0.07
print(popt)
print(np.sqrt(pcov))

plt.xlabel(r"$\nu$ / kHz")
plt.ylabel(r"$U$ / mV")
plt.legend()
plt.tight_layout()
plt.savefig("build/selektiv.pdf")