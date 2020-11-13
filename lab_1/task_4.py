"""" Build figure
"""
import numpy as np  # Подключение numpy под псевдонимом np
import matplotlib.pyplot as plt

x = np.arange(-20, 20, 0.1)
with plt.xkcd():
    plt.plot(x, eval(input('Введите формулу для y (например: x ** 3)\n')))
    plt.title('График "от руки"')

plt.show()

som_list = [(1, 1), (2, 3), (25, 5)]
for i, k in enumerate(som_list):
    print(i, k)
