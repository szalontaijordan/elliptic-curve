from . import equals, add, double


def bits(n):
    while n:
        yield n & 1
        n >>= 1


def times(k, P, field):
    (Fp, p, order, h) = field

    if k % order == 0 or equals(P, (None, None)):
        return None, None

    result = (None, None)
    addend = P

    for bit in bits(k):
        if bit == 1:
            result = add(result, addend, field)
        addend = double(addend, field)

    return result
