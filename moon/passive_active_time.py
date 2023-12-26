import numpy as np
from scipy.optimize import fsolve

v2, g, Ve, m2, P, b, h2, j = -0.2, 1.622, 0, 8710, 46696, 46696 / 2980, 13500, 2980

f1 = lambda tp, ta: v2 - g * (ta + tp) - j * np.log((m2 - b * ta) / m2) - Ve
f2 = lambda tp, ta: h2 + v2 * (ta + tp) - g / 2 * (ta + tp) ** 2 - j * (
        (ta - m2 / b) * (np.log(1 - b / m2 * ta) - 1) - m2 / b)
f = lambda x: (f1(x[0], x[1]), f2(x[0], x[1]))

t23e = fsolve(f, [1, 1])

print(t23e)
