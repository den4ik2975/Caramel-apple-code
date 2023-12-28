import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import solve_ivp

# Constants
m0 = 0  # initial mass, kg
P = 46696  # thrust, N
J = 2980  # specific impulse, m/s
g = 1.622  # gravitational acceleration, m/s^2
theta0 = np.pi / 2  # initial angle, radians

# Initial conditions
y0 = 90000  # initial y-position, m
x0 = 0  # initial x-position, m
V0 = 1666  # initial velocity, m/s


# Define the system of differential equations
def rocket_motion(t, state, P, J, g, m0):
    y, x, V, theta, mt = state
    mass = 14710 - mt
    dydt = -V * np.cos(theta)
    dxdt = V * np.sin(theta)
    dVdt = -P / mass + g * np.cos(theta)
    dthetadt = -g * np.sin(theta) / V
    dmdt = P / J
    return [dydt, dxdt, dVdt, dthetadt, dmdt]


# Initial state vector
initial_state = [y0, x0, V0, theta0, m0]

# Time span for the simulation (start and end)
t_span = (0, 500)  # end time is arbitrary, can be adjusted as needed
t = np.linspace(0, 450, 450)

# Solve the system of differential equations
solution = solve_ivp(
    rocket_motion,
    t_span=t_span,
    y0=initial_state,
    args=(P, J, g, m0),
    method='RK45',
    dense_output=True,
    t_eval=t
)

h = solution.y[0]
v = solution.y[2]

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
