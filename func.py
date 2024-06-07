import math

def exponential(base, x):
    return math.pow(base, x)

def poly(coef, x):
    deg = len(coef) - 1

    result = 0
    for i in range(deg + 1):
        result += math.pow(x, i) * coef[deg - i]
    return result

def f(x, func_conf):
    base = func_conf['base']

    coef = func_conf['coef']

    return exponential(base, x) - poly(coef, x)

def df(x, func_conf):
    delta = 1e-6
    return (f(x + delta, func_conf) - f(x - delta, func_conf)) / (delta * 2)
    