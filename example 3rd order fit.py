import numpy as np
import matplotlib.pyplot as plt

# Generate some data
x = np.linspace(0, 10, 100)
y = np.sin(x) + np.random.randn(100)

# Fit a 3rd order polynomial to the data
coefficients = np.polyfit(x, y, 3)

# Plot the data and the fitted polynomial
plt.plot(x, y, 'o', label='Data')
plt.plot(x, np.polyval(coefficients, x), '-', label='Fitted polynomial')
plt.legend()
plt.show()