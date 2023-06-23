import logging

from entrypoint2 import entrypoint

__version__ = "3.2"


@entrypoint
def add(one: int, two=4, three=False):
    """This function adds two numbers.

    :param one: first number to add
    :param two: second number to add
    :param three: print hello if True
    :rtype: int
    """

    # 'one' and 'two' are converted to int
    s = one + two

    logging.debug(s)
    print(s)
    if three:
        print("hello")
    return s
