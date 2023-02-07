def distance_between_points(a, b):
    x1, y1 = a
    x2, y2 = b
    return ( (x2 - x1)**2 + (y2 - y1)**2 )**0.5

# OR:

import math


def distance_between_points(a, b):
    a = [a.x, b.y]
    b = [b.x, b.y]
    return math.dist(a, b)