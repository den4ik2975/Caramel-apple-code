import math

import matplotlib.pyplot as plt
import numpy as np

P0 = 101325
H = 5600
MOLAR_AIR = 28.9 * 10 ** -3
R = 287

LAYERS = {
    1: (0, 11000),
    2: (11000, 14000),
    3: (14000, 27000),
    4: (27000, 39000),
    5: (39000, 43000),
    6: (43000, 70000)
}

TEMP_GRADIENT = {
    1: -7.3,
    2: 4,
    3: 1,
    4: 3.6,
    5: -1.5,
    6: -3
}

TEMPERATURES = {
    1: 285,
    2: 205,
    3: 217,
    4: 230,
    5: 273,
    6: 267
}


def get_layer(h):
    if 0 <= h < 11000:
        return 1
    if 11000 <= h < 14000:
        return 2
    if 14000 <= h < 27000:
        return 3
    if 27000 <= h < 39000:
        return 4
    if 39000 <= h < 43000:
        return 5
    if 43000 <= h <= 70000:
        return 6
    if h >= 70000:
        return 6


# Ts = T'
def Ts(h):
    return TEMPERATURES[get_layer(h)] + TEMP_GRADIENT[get_layer(h)] * (h - LAYERS[get_layer(h)][0]) / 1000


def p(h):
    return P0 * math.exp(-h / H)


def ro(h):
    return p(h) * MOLAR_AIR / (Ts(h) * R)


x = np.linspace(1, 75000, 75000)
y = [ro(h) * 1000 for h in x]

y1 = [Ts(h) for h in x]

plt.style.use('dark_background')
plt.rcParams['figure.figsize'] = [10, 7]
plt.rc('axes', edgecolor='#FFE9CC')
plt.rc('axes', labelcolor='#FFE9CC')
plt.rc('axes', titlecolor='#FFE9CC')
plt.rc('xtick', color='#FFE9CC')
plt.rc('ytick', color='#FFE9CC')
plt.xticks(range(160, 301, 10))

plt.title("График зависимости температуры от высоты")
plt.xlabel("Температура")
plt.ylabel("Высота")
plt.plot(y1, x, color="#C24124")

# plt.plot(x, y1, color="blue")
plt.show()
