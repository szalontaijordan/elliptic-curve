from ec.elliptic_curve import times


def ecdh(from_pk, sk, Fp):
    shared_key = times(sk, from_pk, Fp)
    return shared_key[0]
