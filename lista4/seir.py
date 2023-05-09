import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import odeint
import argparse


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

    (S, E, I, R) = sol.T

    plt.plot(t, np.c_[S, E, I, R])
    plt.xlabel("time")
    plt.ylabel("people")
    plt.legend(["Susceptible","Exposed","Infective","Recovered"])
    plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="plots SEIR model")
    parser.add_argument("-N", metavar="N", type=int, default=1000, help="total number of people")
    parser.add_argument("-S0", metavar="S0", type=int, default=999, help="initial number of suspectible people")
    parser.add_argument("-E0", metavar="E0", type=int, default=1, help="initial number of exposed people")
    parser.add_argument("-I0", metavar="I0", type=int, default=0, help="initial number of infective people")
    parser.add_argument("-R0", metavar="R0", type=int, default=0, help="initial number of recovered people")
    parser.add_argument("-beta", metavar="beta", type=float, default=1.34, help="infectious rate")
    parser.add_argument("-sigma", metavar="sigma", type=float, default=0.19, help="incubation rate")
    parser.add_argument("-gamma", metavar="gamma", type=float, default=0.34, help="recovery rate")

    args = parser.parse_args()
    N = args.N
    S0 = args.S0
    E0 = args.E0
    I0 = args.I0
    R0 = args.R0
    beta = args.beta
    sigma = args.sigma
    gamma = args.gamma

    seir(N, S0, E0, I0, R0, beta, sigma, gamma)