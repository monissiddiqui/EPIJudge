import collections

from test_framework import generic_test
from test_framework.test_failure import PropertyName

Rect = collections.namedtuple('Rect', ('x', 'y', 'width', 'height'))


def intersect_rectangle(r1: Rect, r2: Rect) -> Rect:
    widthIntersect = r1.x <= r2.x <= r1.x + r1.width or r2.x <= r1.x <= r2.x + r2.width
    heightIntersect = r1.y <= r2.y <= r1.y + r1.height or r2.y <= r1.y <= r2.y + r2.height
    if  heightIntersect and widthIntersect :
        l = max(r1.x,r2.x)
        r = min(r1.x+r1.width,r2.x+r2.width)
        b = max(r1.y,r2.y)
        t = min(r1.y + r1.height,r2.y + r2.height)
        if r>l or t > b :
            return Rect(l,b,r-l,t-b)

    return Rect(0,0,-1,-1)

def intersect_rectangle_simple(r1: Rect, r2: Rect) -> Rect:
    l = max(r1.x,r2.x)
    r = min(r1.x+r1.width,r2.x+r2.width)
    b = max(r1.y,r2.y)
    t = min(r1.y + r1.height,r2.y + r2.height)
    if l <= r and b <= t :
        return Rect(l,b,r-l,t-b)
    else :
        return Rect(0,0,-1,-1)


def intersect_rectangle_wrapper(r1, r2):
    return intersect_rectangle_simple(Rect(*r1), Rect(*r2))


def res_printer(prop, value):
    def fmt(x):
        return [x[0], x[1], x[2], x[3]] if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('rectangle_intersection.py',
                                       'rectangle_intersection.tsv',
                                       intersect_rectangle_wrapper,
                                       res_printer=res_printer))
