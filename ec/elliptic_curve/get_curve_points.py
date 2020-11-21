from .is_point import is_point


def get_curve_points(E, field):
    (curve, G) = E
    (Fp, p, n, h) = field
    curve_points = [(None, None)]

    if p > 30:
        print('Fp is too big to calculate all points')
        return curve_points

    for x in Fp:
        for y in Fp:
            if is_point((x, y), curve, field):
                curve_points.append((x, y))

    return curve_points
