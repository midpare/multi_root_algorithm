def newton_raphson(f, df, x0, e, max_iter, func_conf):
    points = [x0]
    for _ in range(max_iter):
        xn = points[-1]

        fxn = f(xn, func_conf)
        dfxn = df(xn, func_conf)

        if dfxn == 0:
            print('0으로 나눌 수 없습니다.')
            return None
        

        if abs(fxn) < e:
            sign = ((points[-1] - points[-2]) * dfxn)
            sign = (abs(sign) / sign) * -1
            return xn
        
        points.append(xn - fxn/dfxn)
    print('최대 반복 횟수에 도달했습니다.')
    return None

def modified_false_position(f, x0, x1, e, max_iter, func_conf):
    fa = f(x0, func_conf)
    fb = f(x1, func_conf)
    if fa * fb > 0:
        raise ValueError("f(a) and f(b) must have opposite signs")
    
    for _ in range(max_iter):
        c = (x0 * fb - x1 * fa) / (fb - fa)
        fc = f(c, func_conf)
        
        if fc * fa < 0:
            x1 = c
            fb = fc
        else:
            x0 = c
            fa = fc
        
        if fc * fa < 0:
            fb /= 2
        else:
            fa /= 2
        
        if abs(fc) < e:
            return c
    return None


def momentum(df, x0, max_iter, max_num, alpha, m, func_conf):
    initial= df(x0, func_conf)
    d = df(x0, func_conf)

    value = []
    for sign in ([-1, 1] if abs(d) / d == 1 else [1, -1]):

        momentums = [0]
        points = [x0]
        
        for _ in range(max_iter):
            last_mom = momentums[-1]
            x = points[-1]
            dfxn = df(x, func_conf)

            new_mom = (m * last_mom) - (alpha * dfxn) * sign
            new_x = x + new_mom
            momentums.append(new_mom)
            points.append(new_x)
            
            if abs(new_x) > max_num:
                value.append(None)
                break
                    
            if initial * df(new_x, func_conf) < 0:
                value.append(new_x)
                break
    

    return value

def poly_to_str(list):
    equation = ""

    degree = len(list) - 1

    for i, coef in enumerate(list):
        if i < len(list) - 1:
            if coef != 0:        
                if equation and coef > 0:
                    equation += " + "
                elif coef < 0:
                    equation += " - "
                    coef = -coef
                if coef == 1 and degree - i > 0:
                    equation += f"x^{degree-i}"
                else:
                    if degree - i == 1:
                        equation += f"{coef}x"
                    else:
                        equation += f"{coef}x^{degree-i}"
        else:
            if coef > 0 and equation:
                equation += f" + {coef}"
            elif coef < 0:
                equation += f" - {-coef}"
            elif not equation:
                equation += f"{coef}"

    return equation

