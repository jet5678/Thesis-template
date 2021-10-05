# Import nesessary modules
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib import rc

# create arrays:
x = np.arange(0,5.1,0.1)

y = 0.65*x**3-4*x**2+4*x+1

z = 0.1*y

# use LaTeX rendering and select font type
rcParams['font.family'] = 'serif'
rc('text', usetex=True)

# create figure 
fig = plt.figure(figsize=(4,3))

# plot graph here:
plt.plot(x, y_1, label = 'Funktion')
plt.fill_between(x,y-z,y+z,alpha = 0.2, color='k',label='Unsicherheit')

# create axis labels
plt.xlabel('Zeit / s')
plt.ylabel('Amplitude / m')

# create legend and grid
plt.grid(alpha = .3)
plt.legend()

# adjust margins 
plt.tight_layout(pad=0.1)

# save Figure at any place
plt.savefig('./Fkt_mit_Unsicherheit.pdf')