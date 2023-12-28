import math

import matplotlib.pyplot as plt
import numpy as np

P0 = 101325
H = 5600


def p(h):
    return P0 * (math.e ** ((-h) / H))


x = np.linspace(1, 70000, 70000)

y = [p(h) for h in x]

plt.style.use('dark_background')
plt.rcParams['figure.figsize'] = [10, 7]
plt.rc('axes', edgecolor='#FFE9CC')
plt.rc('axes', labelcolor='#FFE9CC')
plt.rc('axes', titlecolor='#FFE9CC')
plt.rc('xtick', color='#FFE9CC')
plt.rc('ytick', color='#FFE9CC')
plt.xlim(10 ** -2, 10 ** 6)
plt.xscale('log')
#plt.xticks(range(10 ** -2, 10 ** 6, ))

plt.title("График зависимости давления от высоты")
plt.xlabel("Давление (П)")
plt.ylabel("Высота (м)")
plt.plot(y, x, color="#C24124")

# plt.plot(x, y1, color="blue")
plt.show()
