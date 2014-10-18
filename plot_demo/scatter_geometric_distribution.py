import matplotlib.pyplot as plt
from numpy.random import rand
import numpy as np

w = np.random.geometric(p=0.1, size=100000)
#x = np.random.geometric(p=0.35, size=1000)
#z = np.random.geometric(p=0.5, size=1000)
print w

plt.hist(w, bins=50, color='red')
#plt.hist(x, bins=50, color='green')
#plt.hist(z, bins=50, color='blue')

plt.legend()
plt.grid(True)

plt.show()
