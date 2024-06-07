from methods import momentum, modified_false_position, newton_raphson

def get_secant(f, df, x0, x1, roots, poles, conf):
    for p in poles:
        if abs(p - x1) < conf['max_pole_diff']:
            return
        
    e = conf["e"]
    max_iter = conf["max_iter"]
    max_num = conf['max_num']
    alpha = conf['alpha']
    m = conf['m']

    func_conf = conf['func_conf']

    poles.append(x1)

    if f(x0, func_conf) * f(x1, func_conf) >= 0:
        _, inv_x2 = momentum(df, x1, max_iter, max_num, alpha, m, func_conf)

        r1 = modified_false_position(f, x1, inv_x2, e, max_iter, func_conf)
        roots.append(r1)
        poles.append(inv_x2)

        x1 = inv_x2

    r = modified_false_position(f, x0, x1, e, max_iter, func_conf)

    roots.append(r)

    x2, inv_x2 = momentum(df, r, max_iter, max_num, alpha, m, func_conf)

    get_secant(f, df, x0, inv_x2, roots, poles, conf)
    get_secant(f, df, x2, x1, roots, poles, conf)

def get_roots(f, df, conf, roots, poles):
    x1 = conf["x0"]
    e = conf["e"]
    max_iter = conf["max_iter"]
    max_num = conf['max_num']
    alpha = conf['alpha']
    m = conf['m']


    func_conf = conf['func_conf']

    r1 = newton_raphson(f, df, x1, e, max_iter, func_conf)
    if not r1:
        return
    
    roots.append(r1)
    x0, _ = momentum(df, r1, max_iter, max_num, alpha, m, func_conf)

    if not x0:
        return
    
    poles.append(x0)
    r2 = newton_raphson(f, df, x0, e, max_iter, func_conf)

    if not r2:
        return
    
    roots.append(r2)
    x1, inv_x1 = momentum(df, r2, max_iter, max_num, alpha, m, func_conf)

    if inv_x1:
        get_secant(f, df, x0, inv_x1, roots, poles, conf)

    if x1:
        poles.append(x1)
        conf['x0'] = x1
        get_roots(f, df, conf, roots, poles)

    return roots

