import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


def seir(N, S0, E0, I0, R0, beta, sigma, gamma):
    def dydt(y, t):
        S, E, I, R = y
        return [-beta*S*I/N,
                beta*S*I/N - sigma*E,
                sigma*E - gamma*I,
                gamma*I]
    
    t = np.linspace(0, 100, 1000)

    y0 = (S0, E0, I0, R0)
    sol = odeint(dydt, y0=y0, t=t)

    S, E, I, R = sol.T

    plt.plot(t, np.c_[S, E, I, R])
    plt.show()


if __name__ == "__main__":
    seir(1000, 999, 1, 0, 0, 1.34, 0.19, 0.34) 