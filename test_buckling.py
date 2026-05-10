import numpy as np
from scipy import optimize
def column_stress_error(P, L, E, A, r, c, e, sigma_allow):
    # פרמטרים לדוגמה 
    #A, E, L, r, e, c = 5000, 200000, 3000, 50, 20, 100 
    # נוסחת הסקנט
    sec_term = 1 / np.cos((L/(2*r)) * np.sqrt(P/(E*A)))
    sigma_max = (P/A) * (1 + (e*c/r**2) * sec_term)
    return sigma_max - sigma_allow 

def find_critical_load(L, E, A, r, c, e, sigma_allow):
    P_critical = optimize.newton(lambda P: column_stress_error(P, L, E, A, r, c, e, sigma_allow), 1000)
    return P_critical  
