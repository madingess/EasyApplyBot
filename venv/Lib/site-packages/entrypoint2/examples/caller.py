import logging

import hello  # type: ignore

from entrypoint2 import entrypoint

__version__ = "5.2"


@entrypoint
def f():
    """calls hello"""
    s = hello.add(7, 2)

    logging.debug("logging sum from caller.py:" + s)
    print("printing sum from caller.py:" + s)
