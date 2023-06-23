from __future__ import division

import math
try:
    from typing import List, Tuple, Union
except ImportError:
    pass  # This is fine; it happens on Python 2.6 and before, but type hints aren't supported there anyway.

__version__ = '1.0.7'


# from http://www.roguebasin.com/index.php?title=Bresenham%27s_Line_Algorithm#Python
def getLine(x1, y1, x2, y2):  # type: (int, int, int, int) -> List[Tuple[int, int]]
    """Returns a list of (x, y) tuples of every point on a line between
    (x1, y1) and (x2, y2). The x and y values inside the tuple are integers.

    Line generated with the Bresenham algorithm.

    Args:
      x1 (int, float): The x coordinate of the line's start point.
      y1 (int, float): The y coordinate of the line's start point.
      x2 (int, float): The x coordinate of the line's end point.
      y2 (int, float): The y coordiante of the line's end point.

    Returns:
      [(x1, y1), (x2, y2), (x3, y3), ...]

    Example:
    >>> getLine(0, 0, 6, 6)
    [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)]
    >>> getLine(0, 0, 3, 6)
    [(0, 0), (0, 1), (1, 2), (1, 3), (2, 4), (2, 5), (3, 6)]
    >>> getLine(3, 3, -3, -3)
    [(3, 3), (2, 2), (1, 1), (0, 0), (-1, -1), (-2, -2), (-3, -3)]
    """
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
    points = []
    issteep = abs(y2 - y1) > abs(x2 - x1)
    if issteep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
    rev = False
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        rev = True
    deltax = x2 - x1
    deltay = abs(y2 - y1)
    error = int(deltax / 2)
    y = y1
    ystep = None
    if y1 < y2:
        ystep = 1
    else:
        ystep = -1
    for x in range(x1, x2 + 1):
        if issteep:
            points.append((y, x))
        else:
            points.append((x, y))
        error -= deltay
        if error < 0:
            y += ystep
            error += deltax
    # Reverse the list if the coordinates were reversed
    if rev:
        points.reverse()
    return points


def getPointOnLine(x1, y1, x2, y2, n):  # type: (Union[int, float], Union[int, float], Union[int, float], Union[int, float], Union[int, float]) -> Tuple[Union[int, float], Union[int, float]]
    """Returns the (x, y) tuple of the point that has progressed a proportion
    n along the line defined by the two x, y coordinates.

    Args:
      x1 (int, float): The x coordinate of the line's start point.
      y1 (int, float): The y coordinate of the line's start point.
      x2 (int, float): The x coordinate of the line's end point.
      y2 (int, float): The y coordiante of the line's end point.
      n (int, float): Progress along the line. 0.0 is the start point, 1.0 is the end point. 0.5 is the midpoint. This value can be less than 0.0 or greater than 1.0.

    Returns:
      Tuple of floats for the x, y coordinate of the point.

    Example:
    >>> getPointOnLine(0, 0, 6, 6, 0)
    (0, 0)
    >>> getPointOnLine(0, 0, 6, 6, 1)
    (6, 6)
    >>> getPointOnLine(0, 0, 6, 6, 0.5)
    (3.0, 3.0)
    >>> getPointOnLine(0, 0, 6, 6, 0.75)
    (4.5, 4.5)
    >>> getPointOnLine(3, 3, -3, -3, 0.5)
    (0.0, 0.0)
    >>> getPointOnLine(3, 3, -3, -3, 0.25)
    (1.5, 1.5)
    >>> getPointOnLine(3, 3, -3, -3, 0.75)
    (-1.5, -1.5)
    """
    x = ((x2 - x1) * n) + x1
    y = ((y2 - y1) * n) + y1
    return (x, y)


def _checkRange(n):  # type: (Union[int, float]) -> None
    """Raises ValueError if the argument is not between 0.0 and 1.0."""
    if not 0.0 <= n <= 1.0:
        raise ValueError('Argument must be between 0.0 and 1.0.')


def linear(n):  # type: (Union[int, float]) -> Union[int, float]
    """A linear tween function

    Example:
    >>> linear(0.0)
    0.0
    >>> linear(0.2)
    0.2
    >>> linear(0.4)
    0.4
    >>> linear(0.6)
    0.6
    >>> linear(0.8)
    0.8
    >>> linear(1.0)
    1.0
    """
    _checkRange(n)
    return n


def easeInQuad(n):  # type: (Union[int, float]) -> Union[int, float]
    """A quadratic tween function that begins slow and then accelerates.

    Args:
      n (float): The time progress, starting at 0.0 and ending at 1.0.

    Returns:
      (float) The line progress, starting at 0.0 and ending at 1.0. Suitable for passing to getPointOnLine().
    """
    _checkRange(n)
    return n**2


def easeOutQuad(n):  # type: (Union[int, float]) -> Union[int, float]
    """A quadratic tween function that begins fast and then decelerates.

    Args:
      n (float): The time progress, starting at 0.0 and ending at 1.0.

    Returns:
      (float) The line progress, starting at 0.0 and ending at 1.0. Suitable for passing to getPointOnLine().
    """
    _checkRange(n)
    return -n * (n - 2)


def easeInOutQuad(n):  # type: (Union[int, float]) -> Union[int, float]
    """A quadratic tween function that accelerates, reaches the midpoint, and then decelerates.

    Args:
      n (float): The time progress, starting at 0.0 and ending at 1.0.

    Returns:
      (float) The line progress, starting at 0.0 and ending at 1.0. Suitable for passing to getPointOnLine().
    """
    _checkRange(n)
    if n < 0.5:
        return 2 * n**2
    else:
        n = n * 2 - 1
        return -0.5 * (n * (n - 2) - 1)


def easeInCubic(n):  # type: (Union[int, float]) -> Union[int, float]
    """A cubic tween function that begins slow and then accelerates.

    Args:
      n (float): The time progress, starting at 0.0 and ending at 1.0.

    Returns:
      (float) The line progress, starting at 0.0 and ending at 1.0. Suitable for passing to getPointOnLine().
    """
    _checkRange(n)
    return n**3


def easeOutCubic(n):  # type: (Union[int, float]) -> Union[int, float]
    """A cubic tween function that begins fast and then decelerates.

    Args:
      n (float): The time progress, starting at 0.0 and ending at 1.0.

    Returns:
      (float) The line progress, starting at 0.0 and ending at 1.0. Suitable for passing to getPointOnLine().
    """
    _checkRange(n)
    n -= 1
    return n**3 + 1


def easeInOutCubic(n):  # type: (Union[int, float]) -> Union[int, float]
    """A cubic tween function that accelerates, reaches the midpoint, and then decelerates.

    Args:
      n (float): The time progress, starting at 0.0 and ending at 1.0.

    Returns:
      (float) The line progress, starting at 0.0 and ending at 1.0. Suitable for passing to getPointOnLine().
    """
    _checkRange(n)
    n *= 2
    if n < 1:
        return 0.5 * n**3
    else:
        n -= 2
        return 0.5 * (n**3 + 2)


def easeInQuart(n):  # type: (Union[int, float]) -> Union[int, float]
    """A quartic tween function that begins slow and then accelerates.

    Args:
      n (float): The time progress, starting at 0.0 and ending at 1.0.

    Returns:
      (float) The line progress, starting at 0.0 and ending at 1.0. Suitable for passing to getPointOnLine().
    """
    _checkRange(n)
    return n**4


def easeOutQuart(n):  # type: (Union[int, float]) -> Union[int, float]
    """A quartic tween function that begins fast and then decelerates.

    Args:
      n (float): The time progress, starting at 0.0 and ending at 1.0.

    Returns:
      (float) The line progress, starting at 0.0 and ending at 1.0. Suitable for passing to getPointOnLine().
    """
    _checkRange(n)
    n -= 1
    return -(n**4 - 1)


def easeInOutQuart(n):  # type: (Union[int, float]) -> Union[int, float]
    """A quartic tween function that accelerates, reaches the midpoint, and then decelerates.

    Args:
      n (float): The time progress, starting at 0.0 and ending at 1.0.

    Returns:
      (float) The line progress, starting at 0.0 and ending at 1.0. Suitable for passing to getPointOnLine().
    """
    _checkRange(n)
    n *= 2
    if n < 1:
        return 0.5 * n**4
    else:
        n -= 2
        return -0.5 * (n**4 - 2)


def easeInQuint(n):  # type: (Union[int, float]) -> Union[int, float]
    """A quintic tween function that begins slow and then accelerates.

    Args:
      n (float): The time progress, starting at 0.0 and ending at 1.0.

    Returns:
      (float) The line progress, starting at 0.0 and ending at 1.0. Suitable for passing to getPointOnLine().
    """
    _checkRange(n)
    return n**5


def easeOutQuint(n):  # type: (Union[int, float]) -> Union[int, float]
    """A quintic tween function that begins fast and then decelerates.

    Args:
      n (float): The time progress, starting at 0.0 and ending at 1.0.

    Returns:
      (float) The line progress, starting at 0.0 and ending at 1.0. Suitable for passing to getPointOnLine().
    """
    _checkRange(n)
    n -= 1
    return n**5 + 1


def easeInOutQuint(n):  # type: (Union[int, float]) -> Union[int, float]
    """A quintic tween function that accelerates, reaches the midpoint, and then decelerates.

    Args:
      n (float): The time progress, starting at 0.0 and ending at 1.0.

    Returns:
      (float) The line progress, starting at 0.0 and ending at 1.0. Suitable for passing to getPointOnLine().
    """
    _checkRange(n)
    n *= 2
    if n < 1:
        return 0.5 * n**5
    else:
        n -= 2
        return 0.5 * (n**5 + 2)


def easeInPoly(n, degree=2):  # type: (Union[int, float], Union[int, float]) -> Union[int, float]
    """A polynomial tween function of given degree that begins slow and then accelerates.

    Args:
      n (float): The time progress, starting at 0.0 and ending at 1.0.

    Returns:
      (float) The line progress, starting at 0.0 and ending at 1.0. Suitable for passing to getPointOnLine().
    """
    _checkRange(n)
    if not isinstance(degree, (int, float)) or degree < 0:
        raise ValueError('degree argument must be a positive number.')
    return n**degree


def easeOutPoly(n, degree=2):  # type: (Union[int, float], Union[int, float]) -> Union[int, float]
    """A polynomial tween function of given degree that begins fast and then decelerates.

    Args:
      n (float): The time progress, starting at 0.0 and ending at 1.0.

    Returns:
      (float) The line progress, starting at 0.0 and ending at 1.0. Suitable for passing to getPointOnLine().
    """
    _checkRange(n)
    if not isinstance(degree, (int, float)) or degree < 0:
        raise ValueError('degree argument must be a positive number.')
    return 1 - abs((n - 1) ** degree)


def easeInOutPoly(n, degree=2):  # type: (Union[int, float], Union[int, float]) -> Union[int, float]
    """A polynomial tween function of given degree that accelerates, reaches the midpoint, and then decelerates.

    Args:
      n (float): The time progress, starting at 0.0 and ending at 1.0.

    Returns:
      (float) The line progress, starting at 0.0 and ending at 1.0. Suitable for passing to getPointOnLine().
    """
    _checkRange(n)
    if not isinstance(degree, (int, float)) or degree < 0:
        raise ValueError('degree argument must be a positive number.')

    n *= 2
    if n < 1:
        return 0.5 * n**degree
    else:
        n -= 2
        return 1 - 0.5 * abs(n**degree)


def easeInSine(n):  # type: (Union[int, float]) -> Union[int, float]
    """A sinusoidal tween function that begins slow and then accelerates.

    Args:
      n (float): The time progress, starting at 0.0 and ending at 1.0.

    Returns:
      (float) The line progress, starting at 0.0 and ending at 1.0. Suitable for passing to getPointOnLine().
    """
    _checkRange(n)
    return -1 * math.cos(n * math.pi / 2) + 1


def easeOutSine(n):  # type: (Union[int, float]) -> Union[int, float]
    """A sinusoidal tween function that begins fast and then decelerates.

    Args:
      n (float): The time progress, starting at 0.0 and ending at 1.0.

    Returns:
      (float) The line progress, starting at 0.0 and ending at 1.0. Suitable for passing to getPointOnLine().
    """
    _checkRange(n)
    return math.sin(n * math.pi / 2)


def easeInOutSine(n):  # type: (Union[int, float]) -> Union[int, float]
    """A sinusoidal tween function that accelerates, reaches the midpoint, and then decelerates.

    Args:
      n (float): The time progress, starting at 0.0 and ending at 1.0.

    Returns:
      (float) The line progress, starting at 0.0 and ending at 1.0. Suitable for passing to getPointOnLine().
    """
    _checkRange(n)
    return -0.5 * (math.cos(math.pi * n) - 1)


def easeInExpo(n):  # type: (Union[int, float]) -> Union[int, float]
    """An exponential tween function that begins slow and then accelerates.

    Args:
      n (float): The time progress, starting at 0.0 and ending at 1.0.

    Returns:
      (float) The line progress, starting at 0.0 and ending at 1.0. Suitable for passing to getPointOnLine().
    """
    _checkRange(n)
    if n == 0:
        return 0
    else:
        return 2 ** (10 * (n - 1))


def easeOutExpo(n):  # type: (Union[int, float]) -> Union[int, float]
    """An exponential tween function that begins fast and then decelerates.

    Args:
      n (float): The time progress, starting at 0.0 and ending at 1.0.

    Returns:
      (float) The line progress, starting at 0.0 and ending at 1.0. Suitable for passing to getPointOnLine().
    """
    _checkRange(n)
    if n == 1:
        return 1
    else:
        return -(2 ** (-10 * n)) + 1


def easeInOutExpo(n):  # type: (Union[int, float]) -> Union[int, float]
    """An exponential tween function that accelerates, reaches the midpoint, and then decelerates.

    Args:
      n (float): The time progress, starting at 0.0 and ending at 1.0.

    Returns:
      (float) The line progress, starting at 0.0 and ending at 1.0. Suitable for passing to getPointOnLine().
    """
    _checkRange(n)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        n *= 2
        if n < 1:
            return 0.5 * 2 ** (10 * (n - 1))
        else:
            n -= 1
            # 0.5 * (-() + 2)
            return 0.5 * (-1 * (2 ** (-10 * n)) + 2)


def easeInCirc(n):  # type: (Union[int, float]) -> Union[int, float]
    """A circular tween function that begins slow and then accelerates.

    Args:
      n (float): The time progress, starting at 0.0 and ending at 1.0.

    Returns:
      (float) The line progress, starting at 0.0 and ending at 1.0. Suitable for passing to getPointOnLine().
    """
    _checkRange(n)
    return -1 * (math.sqrt(1 - n * n) - 1)


def easeOutCirc(n):  # type: (Union[int, float]) -> Union[int, float]
    """A circular tween function that begins fast and then decelerates.

    Args:
      n (float): The time progress, starting at 0.0 and ending at 1.0.

    Returns:
      (float) The line progress, starting at 0.0 and ending at 1.0. Suitable for passing to getPointOnLine().
    """
    _checkRange(n)
    n -= 1
    return math.sqrt(1 - (n * n))


def easeInOutCirc(n):  # type: (Union[int, float]) -> Union[int, float]
    """A circular tween function that accelerates, reaches the midpoint, and then decelerates.

    Args:
      n (float): The time progress, starting at 0.0 and ending at 1.0.

    Returns:
      (float) The line progress, starting at 0.0 and ending at 1.0. Suitable for passing to getPointOnLine().
    """
    _checkRange(n)
    n *= 2
    if n < 1:
        return -0.5 * (math.sqrt(1 - n**2) - 1)
    else:
        n -= 2
        return 0.5 * (math.sqrt(1 - n**2) + 1)


def easeInElastic(n, amplitude=1, period=0.3):  # type: (Union[int, float], Union[int, float], Union[int, float]) -> Union[int, float]
    """An elastic tween function that begins with an increasing wobble and then snaps into the destination.

    Args:
      n (float): The time progress, starting at 0.0 and ending at 1.0.

    Returns:
      (float) The line progress, starting at 0.0 and ending at 1.0. Suitable for passing to getPointOnLine().
    """
    _checkRange(n)
    return 1 - easeOutElastic(1 - n, amplitude=amplitude, period=period)


def easeOutElastic(n, amplitude=1, period=0.3):  # type: (Union[int, float], Union[int, float], Union[int, float]) -> Union[int, float]
    """An elastic tween function that overshoots the destination and then "rubber bands" into the destination.

    Args:
      n (float): The time progress, starting at 0.0 and ending at 1.0.

    Returns:
      (float) The line progress, starting at 0.0 and ending at 1.0. Suitable for passing to getPointOnLine().
    """
    _checkRange(n)

    if amplitude < 1:
        amplitude = 1
        s = period / 4
    else:
        s = period / (2 * math.pi) * math.asin(1 / amplitude)

    return amplitude * 2 ** (-10 * n) * math.sin((n - s) * (2 * math.pi / period)) + 1


def easeInOutElastic(n, amplitude=1, period=0.5):  # type: (Union[int, float], Union[int, float], Union[int, float]) -> Union[int, float]
    """An elastic tween function wobbles towards the midpoint.

    Args:
      n (float): The time progress, starting at 0.0 and ending at 1.0.

    Returns:
      (float) The line progress, starting at 0.0 and ending at 1.0. Suitable for passing to getPointOnLine().
    """
    _checkRange(n)
    n *= 2
    if n < 1:
        return easeInElastic(n, amplitude=amplitude, period=period) / 2
    else:
        return easeOutElastic(n - 1, amplitude=amplitude, period=period) / 2 + 0.5


def easeInBack(n, s=1.70158):  # type: (Union[int, float], Union[int, float]) -> Union[int, float]
    """A tween function that backs up first at the start and then goes to the destination.

    Args:
      n (float): The time progress, starting at 0.0 and ending at 1.0.

    Returns:
      (float) The line progress, starting at 0.0 and ending at 1.0. Suitable for passing to getPointOnLine().
    """
    _checkRange(n)
    return n * n * ((s + 1) * n - s)


def easeOutBack(n, s=1.70158):  # type: (Union[int, float], Union[int, float]) -> Union[int, float]
    """A tween function that overshoots the destination a little and then backs into the destination.

    Args:
      n (float): The time progress, starting at 0.0 and ending at 1.0.

    Returns:
      (float) The line progress, starting at 0.0 and ending at 1.0. Suitable for passing to getPointOnLine().
    """
    _checkRange(n)
    n -= 1
    return n * n * ((s + 1) * n + s) + 1


def easeInOutBack(n, s=1.70158):  # type: (Union[int, float], Union[int, float]) -> Union[int, float]
    """A "back-in" tween function that overshoots both the start and destination.

    Args:
      n (float): The time progress, starting at 0.0 and ending at 1.0.

    Returns:
      (float) The line progress, starting at 0.0 and ending at 1.0. Suitable for passing to getPointOnLine().
    """
    _checkRange(n)
    n *= 2
    if n < 1:
        s *= 1.525
        return 0.5 * (n * n * ((s + 1) * n - s))
    else:
        n -= 2
        s *= 1.525
        return 0.5 * (n * n * ((s + 1) * n + s) + 2)


def easeInBounce(n):  # type: (Union[int, float]) -> Union[int, float]
    """A bouncing tween function that begins bouncing and then jumps to the destination.

    Args:
      n (float): The time progress, starting at 0.0 and ending at 1.0.

    Returns:
      (float) The line progress, starting at 0.0 and ending at 1.0. Suitable for passing to getPointOnLine().
    """
    _checkRange(n)
    return 1 - easeOutBounce(1 - n)


def easeOutBounce(n):  # type: (Union[int, float]) -> Union[int, float]
    """A bouncing tween function that hits the destination and then bounces to rest.

    Args:
      n (float): The time progress, starting at 0.0 and ending at 1.0.

    Returns:
      (float) The line progress, starting at 0.0 and ending at 1.0. Suitable for passing to getPointOnLine().
    """
    _checkRange(n)
    if n < (1 / 2.75):
        return 7.5625 * n * n
    elif n < (2 / 2.75):
        n -= 1.5 / 2.75
        return 7.5625 * n * n + 0.75
    elif n < (2.5 / 2.75):
        n -= 2.25 / 2.75
        return 7.5625 * n * n + 0.9375
    else:
        n -= 2.65 / 2.75
        return 7.5625 * n * n + 0.984375


def easeInOutBounce(n):  # type: (Union[int, float]) -> Union[int, float]
    """A bouncing tween function that bounces at the start and end.

    Args:
      n (float): The time progress, starting at 0.0 and ending at 1.0.

    Returns:
      (float) The line progress, starting at 0.0 and ending at 1.0. Suitable for passing to getPointOnLine().
    """
    _checkRange(n)
    if n < 0.5:
        return easeInBounce(n * 2) * 0.5
    else:
        return easeOutBounce(n * 2 - 1) * 0.5 + 0.5
