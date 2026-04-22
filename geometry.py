import math

def triangle_distances(a, b, c):
    d_ab = abs(a - b)
    d_bc = abs(b - c)
    d_ac = math.sqrt((a - b)**2 + (c - b)**2)
    
    return {
        "d_ab": d_ab,
        "d_bc": d_bc,
        "d_ac": d_ac
    }
