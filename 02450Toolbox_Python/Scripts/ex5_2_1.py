# exercise 5.2.1

import numpy as np
from matplotlib.pyplot import figure, plot, xlabel, ylabel, title, show

# Number of data objects
N = 100

# Attribute values
X = np.array(range(N))

# Noise
eps_mean, eps_std = 0, 0.1
eps = np.array(eps_std * np.random.randn(N) + eps_mean)

# Model parameters
w0 = -0.5
w1 = 0.01

# Outputs
y = w0 + w1 * X + eps

# Make a scatter plot
figure()
plot(X, y, 'o')
xlabel('X');
ylabel('y')
title('Illustration of a linear relation with noise')

show()

print('Ran Exercise 5.2.1')
