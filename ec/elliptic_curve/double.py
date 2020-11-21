from .equals import equals
from ec.finite_field import inv


def double(P, field):
    (Fp, p, n, h) = field
    if equals(P, (None, None)):
        return P

    (xp, yp) = P
    m = ((3*xp**2) * inv(2*yp, p)) % p

    xr = (m**2 - 2*xp) % p
    yr = (m*(xp - xr) - yp) % p

    return int(xr), int(yr)
