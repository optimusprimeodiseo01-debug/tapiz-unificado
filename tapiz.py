import numpy as np
import sympy as sp

def generate_primes(n):
    primes = list(sp.primerange(1, 100))[:n]
    return np.array(primes, dtype=float)

def build_T(n):
    primes = generate_primes(n)
    T = np.diag(primes)
    return T

def compute_H(T):
    return np.log(T)

def compute_K(H):
    return H - H.T

def compute_L(H):
    return 1j * (H - H.T)
