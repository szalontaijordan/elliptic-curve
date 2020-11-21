import matplotlib.pyplot as plt
from ec.elliptic_curve import get_curve_points, curve
from ec.finite_field import finite_field
from ec.key_exchange import ecdh, get_key_pair
from ec.digital_signature import ecdsa


def show_example_curve():
    # Bitcoin curve with small p
    Fp = finite_field(
        p=17,
        n=18,
        h=1
    )
    G = (15, 13)
    E = (curve(a=0, b=7), G)

    # Example curve visualization over finite field
    points = get_curve_points(E, Fp)

    x = list(map(lambda x: x[0], points))
    y = list(map(lambda x: x[1], points))

    plt.xticks(Fp[0])
    plt.yticks(Fp[0])
    plt.xlim([0, 17])
    plt.ylim([0, 17])

    # Points
    plt.scatter(x, y)
    # Generator point
    plt.scatter(G[0], G[1], c='red')

    plt.grid(True)
    title = 'a=0, b=7, p=17, G=(15, 13), n=18, h=1'
    plt.title(title)

    plt.show()


def bitcoin_curve():
    Fp = finite_field(
        p=115792089237316195423570985008687907853269984665640564039457584007908834671663,
        n=115792089237316195423570985008687907852837564279074904382605163141518161494337,
        h=1
    )

    G = (
        55066263022277343669578718895168534326250603453777594175500187360389116729240,
        32670510020758816978083085130507043184471273380659243275938904335757337482424
    )

    E = (curve(a=0, b=7), G)

    return E, Fp


def main():
    # Example
    show_example_curve()

    # Get E curve over Fp finite field
    (E, Fp) = bitcoin_curve()

    # Key Pairs for Alice and Bob
    (alice_pk, alice_sk) = get_key_pair(E, Fp)
    (bob_pk, bob_sk) = get_key_pair(E, Fp)

    # Elliptic Curve Diffie-Hellman
    alice_shared_key = ecdh(from_pk=bob_pk, sk=alice_sk, Fp=Fp)
    bob_shared_key = ecdh(from_pk=alice_pk, sk=bob_sk, Fp=Fp)

    # Make sure the shared key is the same
    assert alice_shared_key == bob_shared_key
    print('Successful key exchange between Alice and Bob')
    shared_key = alice_shared_key
    print('Alice & Bob shared key =', shared_key)
    print()

    # Elliptic Curve Digital Signature Algorithm
    message = 'Hello Bob!'
    print('Message =', message)
    print()

    (sign, verify) = ecdsa(E, Fp)
    signature = sign(message, alice_sk)
    print()
    print('Signature =', signature)
    print('Verified =', verify(message, signature, alice_pk))
    print()


if __name__ == '__main__':
    main()
