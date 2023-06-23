import os
import sys

from easyprocess import EasyProcess

from entrypoint2 import entrypoint

python = sys.executable
join = os.path.join
d = os.path.dirname(__file__)

prog = """
from entrypoint2 import entrypoint
@entrypoint
def func(param={value}):
    print(type(param).__name__, repr(param))
"""


def run(value, param):
    cmd = [python, "-c", prog.format(value=value), "--debug"]
    if param == "noval":
        cmd += ["--param"]
    elif param == "nopar":
        cmd += []
    else:
        for p in param.split(","):
            cmd += ["--param", p]
    p = EasyProcess(cmd).call()
    if p.return_code != 0 or p.stderr != "":
        return p.stderr.splitlines()[-1]
    return p.stdout


@entrypoint
def add(param: str):
    s = ""
    for x in [
        "None",
        "'str'",
        "b'bytes'",
        "[]",
        "1",
        "1.1",
        "False",
        "True",
    ]:
        s = "{} -> {}".format(x, run(x, param))
        print(s)
