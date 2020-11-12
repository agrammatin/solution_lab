"""" Build figure
"""
import numpy as np  # Подключение numpy под псевдонимом np
import matplotlib.pyplot as plt

x = np.arange(-10, 10, 0.01)
plt.plot(x, x ** 2 - x - 6)
plt.grid()
print("y(x) = 0 при x = -2 и x = 3")
plt.text(-4, 40, r'$y(x) = 0\ при\ x = -2\ и\ x = 3$')

plt.show()

# -2 3
