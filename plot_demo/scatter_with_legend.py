import matplotlib.pyplot as plt
from numpy.random import rand

X = [x for x in range(10)]
squares = [x**2 for x in range(10)]
Y = squares
plt.scatter(X,Y)

#for color in ['red', 'green', 'yellow', 'magenta', 'blue']:
    #n = 50
    #x, y = rand(2, n)
    #x, y = [0:0, 1:1.2, 2:1.8]
    #scale = 200.0 * rand(n)
    #print scale
    #plt.scatter(x, y, c=color, s=scale, label=color, alpha=0.3, edgecolors='none')

plt.legend()
plt.grid(True)

plt.show()
