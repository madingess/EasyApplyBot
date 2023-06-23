from entrypoint2 import entrypoint


@entrypoint
def add(
    strpar="string",
    bytespar=b"bytes",
    intpar=21,
    floatpar=3.14,
    boolpar=False,
):
    print(f"strpar={repr(strpar)}")
    print(f"bytespar={repr(bytespar)}")
    print(f"intpar={repr(intpar)}")
    print(f"floatpar={repr(floatpar)}")
    print(f"boolpar={repr(boolpar)}")
