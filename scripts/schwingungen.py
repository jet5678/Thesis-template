# Import nesessary modules
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib import rc

# LaTeX-rendering
rcParams['font.family'] = 'serif'
rc('text', usetex=True)

# the plot itself from matplotlib examles
x1 = np.linspace(0.0, 5.0, 1000)
x2 = np.linspace(0.0, 2.5, 1000)
x3 = np.linspace(0.0, 2.5, 10)

y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
y2 = np.cos(2 * np.pi * x2)
y3 = np.cos(2 * np.pi * x3)

# create figure an plot graph
fig = plt.figure(figsize=(4,3))

plt.plot(x1, y1, label = 'gedaempft')
plt.plot(x2, y2, label = 'ungedaempft', c = 'darkorange')
plt.scatter(x3, y3, label = 'Datenpunkte', c = 'darkorange', alpha = .3)

# create axis labels
plt.xlabel('Zeit / s')
plt.ylabel('Amplitude / m')

# create legend and grid
plt.grid(alpha = .3)
plt.legend(loc = 1)

# adjust margins 
plt.tight_layout(pad=0.1)

# save figure in current directory
plt.savefig('./Schwingungen.pdf')