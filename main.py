from func import f, df
from getRoots import get_roots
from methods import poly_to_str

func_conf = {
    "base": 3,
    "coef": [1, 5, 4],
}

conf = {
    'x0': -100,
    'e': 1e-5,
    'max_iter': 10000,
    'max_num': 1e+4,
    'max_pole_diff': 5e-1,
    'alpha': 1e-1,
    'm': 0.4,
    'func_conf': func_conf,
}

roots = []
poles = []

points = get_roots(f, df, conf, roots, poles)

print(f'{func_conf["base"]}^x = {poly_to_str(func_conf['coef'])}의 근')

print()
i = 0
for x in points:
    print(f'x{i}: {x}')
    i += 1
