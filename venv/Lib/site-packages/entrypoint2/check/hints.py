import os
import sys

from easyprocess import EasyProcess

from entrypoint2 import entrypoint

# https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html

python = sys.executable
join = os.path.join
d = os.path.dirname(__file__)

prog = """
from entrypoint2 import entrypoint
from typing import Optional,Any,List,Sequence,Iterable
@entrypoint
def flen(param: {typ}):
    print(type(param).__name__, repr(param))
    """


def run(typ, params):
    cmd = [python, "-c", prog.format(typ=typ), "--debug"] + list(params)
    p = EasyProcess(cmd).call()
    if p.return_code != 0 or p.stderr != "":
        return p.stderr.splitlines()[-1]
    return p.stdout


@entrypoint
def check_hints(*params):
    # TODO: For collections, the type of the collection item is in brackets
    # (Python 3.9+)
    # x: list[int] = [1]
    # x: set[int] = {6, 7}

    # For mappings, we need the types of both keys and values
    # x: dict[str, float] = {'field': 2.0}  # Python 3.9+
    # x: Dict[str, float] = {'field': 2.0}

    # not supported:
    # "Set[str]",
    # "Union[int, str]",
    # "Union[int, float]",
    # "Tuple[int, float, str]",
    # "Tuple[int, ...]",
    # "Callable",
    # "Literal",

    s = ""
    for x in [
        "list[str]",
        "list[bytes]",
        "list[int]",
        "list[float]",
        "list[complex]",
        "list[bool]",
        "str",
        "bytes",
        "int",
        "float",
        "complex",
        "bool",
        "List[str]",
        "List[bytes]",
        "List[int]",
        "List[float]",
        "List[complex]",
        "List[bool]",
        "Sequence[str]",
        "Sequence[bytes]",
        "Sequence[int]",
        "Sequence[float]",
        "Sequence[complex]",
        "Sequence[bool]",
        "Iterable[str]",
        "Iterable[bytes]",
        "Iterable[int]",
        "Iterable[float]",
        "Iterable[complex]",
        "Iterable[bool]",
        "Optional[str]",
        "Optional[bytes]",
        "Optional[int]",
        "Optional[float]",
        "Optional[complex]",
        "Optional[bool]",
        "Any",
    ]:
        s = "{} -> {}".format(x, run(x, params))
        print(s)
