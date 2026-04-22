import numpy as np

def eigen_analysis(L):
    vals, vecs = np.linalg.eig(L)
    return vals, vecs
