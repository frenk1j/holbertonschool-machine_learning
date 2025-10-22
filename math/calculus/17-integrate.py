def poly_integral(poly, C=0):
    # Validate inputs
    if not isinstance(poly, list) or len(poly) == 0:
        return None
    if not isinstance(C, int):
        return None
    for c in poly:
        if not isinstance(c, (int, float)):
            return None

    # Build integral coefficients: start with constant C
    res = [C]
    for power, coef in enumerate(poly):
        new_coef = coef / (power + 1)
        # Cast to int if it is an integer value
        if isinstance(new_coef, float) and new_coef.is_integer():
            new_coef = int(new_coef)
        res.append(new_coef)

    # Trim trailing zeros to keep list as small as possible
    while len(res) > 1 and res[-1] == 0:
        res.pop()

    return res
