def to_readable(se_s, decimals=6):
    se = float(se_s)
    if se > 1e30:
        return f"{se/1e30:.{decimals}f}N"
    elif se > 1e27:
        return f"{se/1e27:.{decimals}f}o"
    elif se > 1e24:
        return f"{se/1e24:.{decimals}f}S"
    elif se > 1e21:
        return f"{se/1e21:.{decimals}f}s"
    elif se > 1e18:
        return f"{se/1e18:.{decimals}f}Q"
    elif se > 1e15:
        return f"{se/1e15:.{decimals}f}q"
    elif se > 1e12:
        return f"{se/1e12:.{decimals}f}T"
    elif se > 1e9:
        return f"{se/1e9:.{decimals}f}B"
    elif se > 1e6:
        return f"{se/1e6:.{decimals}f}M"
    elif se > 1e3:
        return f"{se/1e3:.{decimals}f}K"
    else:
        return f"{se}"

def to_rank(eb):
    if eb > 1e35:
        return "V1"
    elif eb > 1e34:
        return "W3"
    elif eb > 1e33:
        return "W2"
    elif eb > 1e32:
        return "W1"
    elif eb > 1e31:
        return "X3"
    elif eb > 1e30:
        return "X2"
    elif eb > 1e29:
        return "X1"
    elif eb > 1e28:
        return "Y3"
    elif eb > 1e27:
        return "Y2"
    elif eb > 1e26:
        return "Y1"
    elif eb > 1e25:
        return "Z3"
    elif eb > 1e24:
        return "Z2"
    elif eb > 1e23:
        return "Z1"
    else:
        return "na"