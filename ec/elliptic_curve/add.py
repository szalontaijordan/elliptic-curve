from .equals import equals
from .negate import negate
from ec.finite_field import inv


def add(P, Q, field):
    (Fp, p, n, h) = field
    (xp, yp) = P
    (xq, yq) = Q

    if equals(P, Q) or equals(P, negate(Q)):
        return None, None

    if equals(P, (None, None)):
        return Q

    if equals(Q, (None, None)):
        return P

    m = ((yq - yp) * inv(xq - xp, p)) % p

    xr = (m * m - xp - xq) % p
    yr = (m * (xp - xr) - yp) % p

    return int(xr), int(yr)
