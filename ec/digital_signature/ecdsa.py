import random
from hashlib import sha256
from ec.elliptic_curve import times, add
from ec.finite_field import inv


def ecdsa(E, Fp):
    (curve, G) = E
    (fp, p, order, h) = Fp

    def sign(m, sk):
        kE = random.randrange(1, order)
        R = times(kE, G, Fp)
        print('R', R)
        (xr, yr) = R

        r = xr
        s = ((H(m) + r*sk) * inv(kE, order)) % order

        return r, s

    def verify(m, signature, pk):
        (r, s) = signature

        w = inv(s, order)
        u1 = H(m) * w % order
        u2 = r * w % order

        u1G = times(u1, G, Fp)
        u2pk = times(u2, pk, Fp)
        P = add(u1G, u2pk, Fp)
        (xp, yp) = P

        return (xp - r) % order == 0

    return sign, verify


def H(m):
    m_digest = sha256()
    m_digest.update(m.encode('utf-8'))
    return int(m_digest.hexdigest(), 16)
