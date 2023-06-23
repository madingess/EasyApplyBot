import argparse
import inspect
import logging
import re
import sys
import textwrap
from typing import Any, Callable, Iterable, List, Optional, Sequence

PY39PLUS = sys.version_info[0] > 3 or sys.version_info[1] >= 9


def _module_version(func):
    version = None
    for v in "__version__ VERSION version".split():
        version = func.__globals__.get(v)
        if version:
            break
    return version


class _ParagraphPreservingArgParseFormatter(argparse.HelpFormatter):
    def __init__(self, *args, **kwargs):
        super(_ParagraphPreservingArgParseFormatter, self).__init__(*args, **kwargs)
        self._long_break_matcher = argparse._re.compile(r"\n\n+")

    def _fill_text(self, text, width, indent):
        output = []
        for block in self._long_break_matcher.split(text.strip()):
            output.append(
                textwrap.fill(
                    block, width, initial_indent=indent, subsequent_indent=indent
                )
            )
        return "\n\n".join(output + [""])


def _parse_doc(docs):
    """
    Converts a well-formed docstring into documentation
    to be fed into argparse.

    See signature_parser for details.

    shorts: (-k for --keyword -k, or "from" for "frm/from")
    metavars: (FILE for --input=FILE)
    helps: (docs for --keyword: docs)
    description: the stuff before
    epilog: the stuff after
    """

    name = "(?:[a-zA-Z][a-zA-Z0-9-_]*)"

    re_var = re.compile(r"^ *(%s)(?: */(%s))? *:(.*)$" % (name, name))
    re_opt = re.compile(
        r"^ *(?:(-[a-zA-Z0-9]),? +)?--(%s)(?: *=(%s))? *:(.*)$" % (name, name)
    )

    shorts, metavars, helps, description, epilog = {}, {}, {}, "", ""

    if docs:
        prev = ""
        for line in docs.split("\n"):

            line = line.strip()

            # remove starting ':param'
            if line.startswith(":param"):
                line = line[len(":param") :]

            # skip ':rtype:' row
            if line.startswith(":rtype:"):
                continue

            if line.strip() == "----":
                break

            m = re_var.match(line)
            if m:
                if epilog:
                    helps[prev] += epilog.strip()
                    epilog = ""

                if m.group(2):
                    shorts[m.group(1)] = m.group(2)

                helps[m.group(1)] = m.group(3).strip()
                prev = m.group(1)
                previndent = len(line) - len(line.lstrip())
                continue

            m = re_opt.match(line)
            if m:
                if epilog:
                    helps[prev] += epilog.strip()
                    epilog = ""
                name = m.group(2).replace("-", "_")
                helps[name] = m.group(4)
                prev = name

                if m.group(1):
                    shorts[name] = m.group(1)
                if m.group(3):
                    metavars[name] = m.group(3)

                previndent = len(line) - len(line.lstrip())
                continue

            if helps:
                if line.startswith(" " * (previndent + 1)):
                    helps[prev] += "\n" + line.strip()
                else:
                    epilog += "\n" + line.strip()
            else:
                description += "\n" + line.strip()

            if line.strip():
                previndent = len(line) - len(line.lstrip())

    return shorts, metavars, helps, description, epilog


def _listLike(ann, t):
    ret = ann is List[t] or ann is Sequence[t] or ann is Iterable[t]
    if PY39PLUS:
        ret = ret or ann == list[t]
    return ret


def _toStr(x):
    return x


def _toBytes(x):
    return bytes(x, "utf-8")


def _toBool(x):
    return x.strip().lower() not in ["false", "0", "no", ""]


def _useAnnotation(ann, positional=False):
    # https://stackoverflow.com/questions/48572831/how-to-access-the-type-arguments-of-typing-generic
    d = {}
    d["action"] = "store"
    d["type"] = _toStr
    islist = False

    if ann is str:
        pass
    elif ann is bytes:
        d["type"] = _toBytes
    elif ann is bool:
        d["type"] = _toBool
    elif _listLike(ann, str):
        islist = True
    elif _listLike(ann, bytes):
        islist = True
        d["type"] = _toBytes
    elif _listLike(ann, int):
        islist = True
        d["type"] = int
    elif _listLike(ann, float):
        islist = True
        d["type"] = float
    elif _listLike(ann, complex):
        islist = True
        d["type"] = complex
    elif _listLike(ann, bool):
        islist = True
        d["type"] = _toBool
    elif ann is Any:
        pass
    elif ann is Optional[str]:
        pass
    elif ann is Optional[bytes]:
        d["type"] = _toBytes
    elif ann is Optional[int]:
        d["type"] = int
    elif ann is Optional[float]:
        d["type"] = float
    elif ann is Optional[complex]:
        d["type"] = complex
    elif ann is Optional[bool]:
        d["type"] = _toBool
    else:
        d["type"] = ann

    nargs = None
    if islist:
        if positional:
            nargs = "*"
        else:
            d["action"] = "append"

    return d["action"], d["type"], nargs


def _signature_parser(func):
    # args, varargs, varkw, defaults = inspect.getargspec(func)
    (
        args,
        varargs,
        varkw,
        defaults,
        kwonlyargs,
        kwonlydefaults,
        annotations,
    ) = inspect.getfullargspec(func)
    # print(f"func: {func}")
    # print(f"args: {args}")
    # print(f"varargs: {varargs}")
    # print(f"varkw: {varkw}")
    # print(f"defaults: {defaults}")
    # print(f"kwonlyargs: {kwonlyargs}")
    # print(f"kwonlydefaults: {kwonlydefaults}")
    # print(f"annotations: {annotations}")
    if not args:
        args = []

    if not defaults:
        defaults = []

    if varkw:
        raise ValueError("Can't wrap a function with **kwargs")

    # Compulsary positional options
    needed = args[0 : len(args) - len(defaults)]

    # Optional flag options
    params = args[len(needed) :]

    shorts, metavars, helps, description, epilog = _parse_doc(func.__doc__)

    parser = argparse.ArgumentParser(
        description=description,
        epilog=epilog,
        formatter_class=_ParagraphPreservingArgParseFormatter,
    )

    # special flags
    special_flags = []

    special_flags += ["debug"]
    defaults += (False,)
    helps["debug"] = "set logging level to DEBUG"
    if _module_version(func):
        special_flags += ["version"]
        defaults += (False,)
        helps["version"] = "show program's version number and exit"
    params += special_flags

    # Optional flag options  f(p=1)
    used_shorts = set()
    for param, default in zip(params, defaults):
        args = ["--%s" % param.replace("_", "-")]
        short = None
        if param in shorts:
            short = shorts[param]
        else:
            if param not in special_flags and len(param) > 1:
                first_char = param[0]
                if first_char not in used_shorts:
                    used_shorts.add(first_char)
                    short = "-" + first_char
        # -h conflicts with 'help'
        if short and short != "-h":
            args = [short] + args

        d = {"default": default, "dest": param.replace("-", "_")}

        ann = annotations.get(param)
        if param == "version":
            d["action"] = "version"
            d["version"] = _module_version(func)
        elif default is True:
            d["action"] = "store_false"
        elif default is False:
            d["action"] = "store_true"
        elif ann:
            d["action"], d["type"], _ = _useAnnotation(ann)
        elif isinstance(default, list):
            d["action"] = "append"
            d["type"] = _toStr
        elif isinstance(default, str):
            d["action"] = "store"
            d["type"] = _toStr
        elif isinstance(default, bytes):
            d["action"] = "store"
            d["type"] = _toBytes
        elif default is None:
            d["action"] = "store"
            d["type"] = _toStr
        else:
            d["action"] = "store"
            d["type"] = type(default)

        if param in helps:
            d["help"] = helps[param]

        if param in metavars:
            d["metavar"] = metavars[param]
        parser.add_argument(*args, **d)

    # Compulsary positional options  f(p1,p2)
    for need in needed:

        ann = annotations.get(need)
        d = {"action": "store"}
        if ann:
            d["action"], d["type"], nargs = _useAnnotation(ann, positional=True)
            if nargs:
                d["nargs"] = nargs
        else:
            d["type"] = _toStr

        if need in helps:
            d["help"] = helps[need]

        if need in shorts:
            args = [shorts[need]]
        else:
            args = [need]

        parser.add_argument(*args, **d)

    # The trailing arguments  f(*args)
    if varargs:
        d = {"action": "store", "type": _toStr, "nargs": "*"}

        if varargs in helps:
            d["help"] = helps[varargs]

        if varargs in shorts:
            d["metavar"] = shorts[varargs]
        else:
            d["metavar"] = varargs

        parser.add_argument("__args", **d)

    return parser


def _correct_args(func, kwargs):
    """
    Convert a dictionary of arguments including __argv into a list
    for passing to the function.
    """
    args = inspect.getfullargspec(func)[0]
    return [kwargs[arg] for arg in args] + kwargs["__args"]


def entrypoint(func: Callable) -> Callable:
    frame_local = sys._getframe(1).f_locals
    if "__name__" in frame_local and frame_local["__name__"] == "__main__":
        argv = sys.argv[1:]
        # print("__annotations__ ", func.__annotations__)
        # print("__total__", func.__total__)
        parser = _signature_parser(func)
        kwargs = parser.parse_args(argv).__dict__

        # special cli flags

        # --version is handled by ArgParse
        # if kwargs.get('version'):
        #    print module_version(func)
        #    return
        if "version" in kwargs.keys():
            del kwargs["version"]

        # --debug
        FORMAT = "%(asctime)-6s: %(name)s - %(levelname)s - %(message)s"
        if kwargs.get("debug"):
            logging.basicConfig(
                level=logging.DEBUG,
                format=FORMAT,
            )
        del kwargs["debug"]

        if "__args" in kwargs:
            return func(*_correct_args(func, kwargs))
        else:
            return func(**kwargs)

    return func
