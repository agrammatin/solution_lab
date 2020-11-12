"""" Write formula in like look for py
"""
import numpy as np  # Подключение numpy под псевдонимом np
"""
np.pi       число Пи
np.e        чисдо e
np.cos      косинус
np.sin      синус
np.tan      тангенс
np.exp      экспонента
np.log      логарифм натуральный переход: np.log(x) / np.log(2)
"""
x = [1, 10, 1000]
for i in x:
    y = (np.log((1 / (np.e ** np.sin(i + 1))) /
                (5/4 + 1/i**15)) / np.log(1 + i**2))

    print(y)
