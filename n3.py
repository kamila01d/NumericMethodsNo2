import numpy as np
import matplotlib.pyplot as plt
N = 1000
h = 0.01
y = np.zeros(N, dtype=np.float64)
y[0] = 1

def Y(n):

    if n == 0:
        return y[0]
    if n >= 2:
        y_n1 = Y(n-1)
        y_n2 = y[n-2]
        y[n] = 2 * y_n1 - y_n2 - h * h * y_n1

        return y[n]

    if n == 1:
        y_n_minus1 = Y(n-1)
        y_n_plus1 = y[n+1]

        y[n] = (-y_n_minus1 - y_n_plus1) / (-2 + h**2)

        return y[n]

a = Y(N-1)

y[N-1] = (a + 1) / 2
plt.plot(y)
plt.show()

