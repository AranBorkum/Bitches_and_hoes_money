import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import moyal
import scipy.integrate as I

def GetRandomDistribution(n):

# --- Definition of some standard given values -----------------------

  AverageHousePrice = 228147      # [ £ ]
  Gradient          = 78147.0
  Intercept         = 150000

# --- Number holders -------------------------------------------------

  x   = np.linspace(moyal.ppf(0.01), moyal.ppf(0.99), 1000)
  y   = []
  gen = []

# --- Calculating the distribution based on moyal curve --------------

  for i in x:
    y.append(moyal.pdf(i-2))
  
  cdf = I.cumtrapz(y, dx = ((x[-1] - x[1])/len(x)), initial=0)
  for i in range(n):
    gen.append(np.interp(np.random.uniform(), cdf, x))

  return gen

# --- Visual outputs, not totally required ---------------------------

gen = GetRandomDistribution(100000)

plt.figure()
plt.hist(gen, 50)

for i in np.arange(0, 9, 1):
  plt.plot([i, i], [0, 5000], "r--")

plt.xlabel("Arbitrary units with conversion to price")
plt.ylabel("Probability of occrurance")
plt.show()
