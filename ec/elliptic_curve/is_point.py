from .equals import equals


def is_point(p, curve, field):
    if equals(p, (None, None)):
        return True

    (x, y) = p
    (a, b) = curve
    (Fp, prime, n, h) = field

    return (y**2 - x**3 - a*x - b) % prime == 0
