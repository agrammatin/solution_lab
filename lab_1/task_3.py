"""" Build figure
"""
import numpy as np  # Подключение numpy под псевдонимом np
import matplotlib.pyplot as plt

x = np.arange(-20, 20, 0.1)
y = (np.log((x**2 + 1) * (np.exp(-abs(x)/10))) /
     np.log(1 + (np.tan(1/(1 + np.sin(x)**2)))))
plt.title(r'$y=\log_{1+\tan(\frac{1}{1+\sin^2(x)})}{(x^2+1)'
          r'exp(-\frac{|10|}{10})}$', fontsize=18)
plt.plot(x, y)
plt.grid()

plt.show()
