import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import odeint

g = 1.622


def power(t):
    return (t > 432 + 108.26029198) * 46696


# Define the system of differential equations
def model(y, t):
    h, v, mt = y
    mass = 15000 - mt
    dhdt = v
    dvdt = (power(t) / mass) - g
    dmdt = power(t) / 2980
    return [dhdt, dvdt, dmdt]


# Initial conditions
h0 = +13400
v0 = -0.232
mt0 = 6780
y0 = [h0, v0, mt0]

# Time points to solve the DE
t = np.linspace(432, 582, 150)  # for example, from 0 to 500 seconds

# Solve ODE
solution = odeint(model, y0, t)

# The solution is an array with columns for h and v respectively
h = solution[:, 0]
v = solution[:, 1]

# Display the first few results for validation
print(h[:5], v[:5])

plt.style.use('dark_background')
plt.rcParams['figure.figsize'] = [10, 7]
plt.rc('axes', edgecolor='#FFE9CC')
plt.rc('axes', labelcolor='#FFE9CC')
plt.rc('axes', titlecolor='#FFE9CC')
plt.rc('xtick', color='#FFE9CC')
plt.rc('ytick', color='#FFE9CC')
plt.figure(figsize=(10, 5))
plt.plot(t, h, label='Высота от времени', color="#C24124")
plt.title('Зависимость высоты от времени')
plt.xlabel('Время (с)')
plt.ylabel('Высота (м)')
plt.legend()
plt.grid(True)
plt.show()

plt.style.use('dark_background')
plt.rcParams['figure.figsize'] = [10, 7]
plt.rc('axes', edgecolor='#FFE9CC')
plt.rc('axes', labelcolor='#FFE9CC')
plt.rc('axes', titlecolor='#FFE9CC')
plt.rc('xtick', color='#FFE9CC')
plt.rc('ytick', color='#FFE9CC')
plt.figure(figsize=(10, 5))
plt.plot(t, v, label='Скорость от времени', color="#C24124")
plt.title('Зависимость скорости от времени')
plt.xlabel('Время (s)')
plt.ylabel('Скорость ($\\frac{м}{с}$)')
plt.legend()
plt.grid(True)
plt.show()
