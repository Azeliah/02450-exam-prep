# exercise 0.5.1
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, np.pi, 0.01)
f = np.cos(x)

plt.figure(1)
plt.plot(x, f)
plt.xlabel('x')
plt.ylabel('f(x)=cos(x)')
plt.title('The cosine function')
plt.show()
