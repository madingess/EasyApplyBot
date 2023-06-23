from entrypoint2 import entrypoint


@entrypoint
def func(
    strpar: str,
    bytespar: bytes,
    intpar: int,
    floatpar: float,
    boolpar: bool,
    listpar: list[int],
):
    print(f"strpar={repr(strpar)}")
    print(f"bytespar={repr(bytespar)}")
    print(f"intpar={repr(intpar)}")
    print(f"floatpar={repr(floatpar)}")
    print(f"boolpar={repr(boolpar)}")
    print(f"listpar={repr(listpar)}")
