import numpy as np
from scipy import optimize

def column_stress_error(P, L, E, A, r, c, e, sigma_allow):
    # חישוב הדרגתי כדי למנוע טעויות בסוגריים
    inside_sqrt = P / (E * A)
    inside_cos = (L / (2 * r)) * np.sqrt(inside_sqrt)
    
    # חישוב הסקאנט
    sec_term = 1 / np.cos(inside_cos)
    
    # חישוב המאמץ המקסימלי
    sigma_max = (P / A) * (1 + (e * c / r**2) * sec_term)
    
    return sigma_max - sigma_allow 

def find_critical_load(L, E, A, r, c, e, sigma_allow):
    # ניסיון הרצה עם ניחוש ראשוני - וודא שהיחידות מתאימות ל-500,000
    try:
        P_critical = optimize.newton(column_stress_error, 500000, args=(L, E, A, r, c, e, sigma_allow))
        return P_critical
    except Exception as e:
        return f"Error: {e}"
