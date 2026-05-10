import numpy as np
from scipy.optimize import bisect

def find_critical_load(L, E, A, r, c, e, sigma_allow):

    # P_euler = (pi^2 * E * I) / L^2,  where I = A * r^2
    P_euler = (np.pi ** 2 * E * A * r ** 2) / (L ** 2)

    def f(P):
        if P <= 0:
            return -sigma_allow
        theta = (L / (2 * r)) * np.sqrt(P / (E * A))
        secant_val = 1.0 / np.cos(theta)
        sigma_max = (P / A) * (1 + (e * c / r ** 2) * secant_val)
        return sigma_max - sigma_allow

    P_critical = bisect(f, 1e-5, 1 * P_euler)
    return float(P_critical)
