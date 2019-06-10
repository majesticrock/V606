import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from uncertainties import ufloat
import uncertainties.unumpy as unp


mu0 = 1.256 * 10**(-6)
muB= 9.274 * 10**(-24)
g = np.array([0.73, 2.0, 1.33, 0.73])
N = np.array([2.59, 2.46, 2.52, 1.38]) * 10**(28)
J = np.array([4.5, 3.5, 7.5, 4])
k = 1.38 * 10**(-23)
T = 293.15
chi = mu0 * muB**2 * g**2 * N * J * (J + 1)/(3 * k * T)
print(chi)