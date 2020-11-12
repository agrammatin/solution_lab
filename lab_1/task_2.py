"""" Build figure
"""
import numpy as np  # Подключение numpy под псевдонимом np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d


x = np.arange(-10, 10.01, 0.01)
plt.plot(x, x ** 2)
plt.title(r'$y=\log_{1+x^{2}}\frac{\frac{1}{e^{\sin^x+1}}}{\frac{4}{5}'
          r'+\frac{1}{x^{15}}}$', fontsize=14)
plt.grid(True)

fg = plt.figure(2)
# plt.plot(x, np.sin(x), x, np.cos(x), x, -x) # несколько графиков
plt.plot(x, np.sin(x), label=r'$f_1(x)=\sin(x)$')   # Разметка LaTeX
plt.plot(x, np.cos(x), label=r'$f_2(x)=\cos(x)$')
plt.plot(x, -x, label=r'$f_3(x)=-x$')
plt.xlabel(r'$x$', fontsize=14)
plt.ylabel(r'$f(x)$', fontsize=14)
plt.title(r'$f_1(x)=\sin(x),\ f_2(x)=\cos(x),\ f_3(x)=-x$')
plt.legend(loc='best', fontsize=12)
plt.grid(True)

fgg = plt.figure(3, figsize=(10, 10))
# subplot 1
sp_1 = plt.subplot(221)
plt.plot(x, np.sin(x))
plt.title(r'$\sin(x)$')
plt.grid(True)

# subplot 2
sp_2 = plt.subplot(222)
plt.plot(x, np.cos(x), 'g')
plt.axis('equal')
plt.grid(True)
plt.title(r'$\cos(x)$')

# subplot 3
t = np.arange(-10, 11, 1)
sp_3 = plt.subplot(223)
plt.plot(x, x ** 2, t, t ** 2, 'ro')
plt.title(r'$x^2$')

# subplot 4
sp_4 = plt.subplot(224)
plt.plot(x, x)
sp_4.spines['right'].set_position('center')
# sp_4.spines['bottom'].set_position('center')
plt.title(r'$x$')
plt.grid(True)

fig_4 = plt.figure(4)
plt.subplot(111, polar=True)
phi = np.arange(0, 2*np.pi, 0.01)
rho = 2*phi
plt.plot(phi, rho, lw=2)

fig_5 = plt.figure(5)
tt = np.arange(0, 2*np.pi, 0.01)
r = 4
plt.plot(r*np.sin(tt), r*np.cos(tt), lw=3)
plt.axis('equal')
plt.grid(True)

fig_6 = axes3d.Axes3D(plt.figure())
i = np.arange(-1, 1, 0.01)
X, Y = np.meshgrid(i, i)
Z = X**2 - Y**2
fig_6.plot_wireframe(X, Y, Z, rstride=10, cstride=10)

fig_7 = plt.figure(7)
mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)
# the histogram of the data
n, bins, patches = plt.hist(x, 50, density=True, facecolor='g', alpha=0.75)
plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(50, .030, r'$\mu=100,\ \sigma=15$')
plt.text(50, .034, r'$\varphi_{\mu,\sigma^2}(x) = \frac{1}{\sigma\sqrt{2\pi}}'
                   r' \,e^{ -\frac{(x- \mu)^2}{2\sigma^2}} = \frac{1}{\sigma}'
                   r' \varphi\left(\frac{x - \mu}{\sigma}\right),'
                   r'\quad x\in\mathbb{R}$', fontsize=14, color='red')
plt.axis([40, 160, 0, 0.04])
plt.grid(True)

fig_8 = plt.figure(8)
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.grid(True)

fig_9 = plt.figure(9)
# равномерно распределённые значения от 0 до 5, с шагом 0.2
t_1 = np.arange(0., 5., 0.2)
# красные чёрточки, синие квадраты и зелёные треугольники
plt.plot(t_1, t_1, 'r--', t_1, t_1**2, 'bs', t_1, t_1**3, 'g^')

fig_10 = plt.figure(10, figsize=(6, 6))
data = [33, 25, 20, 12, 10]
plt.axes(aspect=1)
plt.title('Круговая диаграмма', size=14)
plt.pie(data, labels=('Group 1', 'Group 2', 'Group 3', 'Group 4', 'Group 5'))

fig_11 = plt.figure(num=11)
objects = ('A', 'B', 'C', 'D', 'E', 'F')
y_pos = np.arange(len(objects))
performance = [10, 8, 6, 4, 2, 1]
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Value')
plt.title('Bar title')

fig_12 = plt.figure(num=12, )

from matplotlib import cm
def makeData():
    xx = np.arange(-10, 10, 0.1)
    yy = np.arange(-10, 10, 0.1)
    xgrid, ygrid = np.meshgrid(xx, yy)
    zgrid = np.sin(xgrid) * np.sin(ygrid) / (xgrid * ygrid)
    return xgrid, ygrid, zgrid


x, y, z = makeData()
# fig = pylab.figure()
axes = axes3d.Axes3D(fig_12)
axes.plot_surface(x, y, z, rstride=4, cstride=4, cmap=cm.jet)

plt.show()
