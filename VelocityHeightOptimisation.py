import numpy as np
from scipy.optimize import differential_evolution


def Quadratic(a, b, c, x):
    return a*(x**2) + b*(x) + c

def Cubic(a, b, c, d, x):
    return a*(x**3) + b*(x**2) + c*(x) + d


def QuadScore(coefficients, h):
    score = 0
    a, b, c = coefficients

    v = Quadratic(a, b, c, h)
    gradient = np.gradient(v, h)
    score -= gradient[0] #want as high a gradient at the start as possible, and as low a final gradient
    score += abs(0 - gradient[-1])

    score += abs(v[-1] - 7500) #target peak velocity is 7500ms^-1
    score += abs(v[0] - 5) #small bnut non zero target start velocity needed
    return score

def CubeScore(coefficients, h):
    score = 0
    a, b, c, d = coefficients

    v = Cubic(a, b, c, d, h)
    gradient = np.gradient(v, h)
    score -= gradient[0] #want as high a gradient at the start as possible, and as low a final gradient
    score += abs(0 - gradient[-1])

    score += abs(v[-1] - 7500) #target peak velocity is 7500ms^-1
    score += abs(v[0] - 5) #small bnut non zero target start velocity needed
    return score


h = np.arange(0, 100000, 5) #heights go from 0 to 100,000

QuadBounds = [(-0.01, 0.01), (-0.1, 0.1), (0, 200000)]
CubeBounds = [(-0.001, 0.001), (-0.01, 0.01), (-0.1, 0.1), (0, 200000)]

QuadResults = differential_evolution(QuadScore, QuadBounds, args = (h,))
CubeResults = differential_evolution(CubeScore, CubeBounds, args = (h,))

print(f"Best Quadratic values and coefficients: {QuadResults.fun}, {QuadResults.x}")
print(f"Best Cubic values and coefficients: {CubeResults.fun}, {CubeResults.x}")
#Best one was -0.09978162025528937, [-5.01002917e-12  2.51391808e-07  9.99111056e-02  5.00001903e+00] for a cubic